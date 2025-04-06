from agent.agent_core import compiled_graph
from models.email_state import EmailState
from src.langfuse_client import langfuse_handler  # Import the Langfuse callback

# Example legitimate email
legitimate_email = {
    "sender": "john.smith@example.com",
    "subject": "Question about your services",
    "body": "Dear Mr. Hugg, I was referred to you by a colleague and I'm interested in learning more about your consulting services. Could we schedule a call next week? Best regards, John Smith"
}

# Example spam email
spam_email = {
    "sender": "winner@lottery-intl.com",
    "subject": "YOU HAVE WON $5,000,000!!!",
    "body": "CONGRATULATIONS! You have been selected as the winner of our international lottery! To claim your $5,000,000 prize, please send us your bank details and a processing fee of $100."
}

def process_email(email_content):
    """
    Processes an email via the LangGraph compiled graph and logs with Langfuse via callback handler.

    Args:
        email_content (dict): The content of the email.
        email_type (str): Type of email (e.g., 'legitimate', 'spam')
    """
    print(f"\n📩 Processing email...")
    print(f"Email content: {email_content}")

    try:
        result = compiled_graph.invoke(
            input={
                "email": email_content,
                "is_spam": None,
                "spam_reason": None,
                "email_category": None,
                "draft_response": None,
                "messages": []
            },
            config={
                "callbacks": [langfuse_handler],
                "metadata": {
                    "sender": email_content.get("sender")
                }
            }
        )

        print("✅ Email processed successfully!")
        print(result)

    except Exception as e:
        print(f"❌ Error processing email: {e}")


def main():
    """
    The main function of the application.
    """
    # Process the legitimate email
    #process_email(legitimate_email)

    # Process the spam email
    process_email(spam_email)

if __name__ == "__main__":
    main()
