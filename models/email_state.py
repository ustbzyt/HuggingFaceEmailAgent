from typing import TypedDict, List, Dict, Any, Optional

class EmailState(TypedDict):
    # The email being processed
    email: Dict[str, Any]  # Contains subject, sender, body, etc.

    # Category of the email
    email_category: Optional[str]
    
    # Analysis and decisions
    is_spam: Optional[bool]

    # Reason why the email was marked as spam
    spam_reason: Optional[str]

    # Category of the email (inquiry, complaint, etc.)
    email_category: Optional[str]
    
    # Response generation
    draft_response: Optional[str]
    
    # Processing metadata
    messages: List[Dict[str, Any]]  # Track conversation with LLM for analysis
