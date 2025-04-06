from agent.agent_core import compiled_graph
from models.email_state import EmailState
from src.langfuse_client import langfuse  # Import the langfuse client instance

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
    Processes an email, logging the process with Langfuse, and invokes the compiled_graph.

    Args:
        email_content (dict): The content of the email.
    """
    trace = langfuse.trace(name="Process Email")
    try:
        # Your email processing logic here
        print(f"Processing email...")
        print(f"Email content: {email_content}")

        # Invoke the compiled_graph
        result = compiled_graph.invoke({
            "email": email_content,
            "is_spam": None,
            "spam_reason": None,
            "email_category": None,
            "draft_response": None,
            "messages": []
        })
        print(f"Email result:")
        print(result)

        # Example: Add an event to the trace
        trace.event(name="Email Content", input=str(email_content))
        trace.event(name="Graph Result", input=str(result))

    except Exception as e:
        # Handle any errors that occur during processing
        print(f"Error processing email: {e}")
        trace.event(name="Error", level="ERROR", input=str(e))
    finally:
        trace.end()


def main():
    """
    The main function of the application.
    """
    # Process the legitimate email
    print("Processing legitimate email...")
    process_email(legitimate_email)

    # Process the spam email
    print("Processing spam email...")
    process_email(spam_email)

if __name__ == "__main__":
    main()
