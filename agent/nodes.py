from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from models.email_state import EmailState
import json

def read_email(state: EmailState):
    """Alfred reads and logs the incoming email"""
    email = state["email"]
    print(f"Alfred is processing an email from {email['sender']} with subject: {email['subject']}")
    return {}


def classify_email(state: EmailState, model: ChatOllama):
    """Classifies the email as spam or legitimate using an LLM."""
    email = state["email"]

    prompt = f"""
    You are Alfred, a helpful butler. Analyze the email and classify it as either SPAM or LEGITIMATE.

    Email:
    From: {email['sender']}
    Subject: {email['subject']}
    Body: {email['body']}

    Respond in the following JSON format:
    {{
        "classification": "SPAM" or "LEGITIMATE",
        "reason": "Explanation of your decision",
        "category": "inquiry/complaint/thank you/request/information" (only if LEGITIMATE)
    }}
    """

    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)
    response_text = response.content.strip()

    try:
        result = json.loads(response_text)
        classification = result.get("classification", "").strip().lower()
        is_spam = classification == "spam"
        spam_reason = result.get("reason") if is_spam else None
        email_category = result.get("category") if not is_spam else None
    except Exception as e:
        print("Error parsing model response:", e)
        is_spam = True
        spam_reason = "Could not parse LLM response."
        email_category = None

    new_messages = state.get("messages", []) + [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response.content}
    ]

    return {
        "is_spam": is_spam,
        "spam_reason": spam_reason,
        "email_category": email_category,
        "messages": new_messages
    }


def handle_spam(state: EmailState):
    """Moves spam emails to the spam folder."""
    print(f"Alfred has marked the email as spam. Reason: {state['spam_reason']}")
    print("The email has been moved to the spam folder.")
    return {}


def draft_response(state: EmailState, model: ChatOllama):
    """Drafts a professional response to a legitimate email."""
    email = state["email"]
    category = state.get("email_category", "general")

    prompt = f"""
    As Alfred the butler, draft a polite preliminary response to this email.

    Email:
    From: {email['sender']}
    Subject: {email['subject']}
    Body: {email['body']}

    This email has been categorized as: {category}

    Draft a brief, professional response that Mr. Hugg can review and personalize before sending.
    """

    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)

    new_messages = state.get("messages", []) + [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response.content}
    ]

    return {
        "draft_response": response.content,
        "messages": new_messages
    }


def notify_mr_hugg(state: EmailState):
    """Displays the email and draft response for Mr. Hugg's review."""
    email = state["email"]

    print("\n" + "=" * 50)
    print(f"Sir, you've received an email from {email['sender']}.")
    print(f"Subject: {email['subject']}")
    print(f"Category: {state['email_category']}")
    print("\nI've prepared a draft response for your review:")
    print("-" * 50)
    print(state["draft_response"])
    print("=" * 50 + "\n")

    return {}


def route_email(state: EmailState) -> str:
    """Routes email to the appropriate handler."""
    return "spam" if state["is_spam"] else "legitimate"
