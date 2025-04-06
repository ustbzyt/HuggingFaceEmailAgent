import os
from langfuse import Langfuse
from typing import Optional

_langfuse_client: Optional[Langfuse] = None

def get_langfuse_client() -> Langfuse:
    """
    Initializes and returns the Langfuse client.

    Raises:
        ValueError: If the Langfuse public key or secret key is not found in environment variables.
    """
    global _langfuse_client
    if _langfuse_client is None:
        public_key = os.environ.get("LANGFUSE_PUBLIC_KEY")
        secret_key = os.environ.get("LANGFUSE_SECRET_KEY")

        if not public_key or not secret_key:
            raise ValueError(
                "Langfuse public key or secret key not found in environment variables."
            )

        _langfuse_client = Langfuse(
            public_key=public_key,
            secret_key=secret_key,
            host="https://cloud.langfuse.com",  # Or your self-hosted instance URL
        )
    return _langfuse_client

langfuse = get_langfuse_client()
