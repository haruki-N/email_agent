from langchain_core.tools import tool


@tool
def write_email(to: str, subject: str, content: str) -> str:
    """Write an email to a recipient."""
    return f"Email sent to {to} with subject {subject} and content {content}"
