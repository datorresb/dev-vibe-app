from typing import Annotated

from langgraph.graph.message import AnyMessage, add_messages
from typing_extensions import TypedDict


class ChatState(TypedDict):
    """Estado del agente conversacional."""

    messages: Annotated[list[AnyMessage], add_messages]
