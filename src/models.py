from pydantic import BaseModel, Field
from typing_extensions import TypeDict, Literal, Annotated
from langchain.chat_models import init_chat_model

llm = init_chat_model("openai:gpt-4o-mini")


class Router(BaseModel):
    """Analyze the unread email and route it according to its content."""

    reasoning: str = Field(
        description="Step-by-step reasoning behind the classification."
    )
    classification: Literal["ignore", "respond", "notify"] = Field(
        description="The classification of an email: 'ignore' for irrelevant emails, "
        "'notify' for important information that doesn't need a response, "
        "'respond' for emails that need a reply",
    )


llm_router = llm.with_structured_output(Router)
