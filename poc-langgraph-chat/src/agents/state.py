"""
State definitions for the conversational agent.

Define aquí todos los estados que usa el grafo.
"""

from typing import Annotated, TypedDict

from langgraph.graph.message import add_messages


class ConversationState(TypedDict):
    """
    Estado principal del agente conversacional.

    Attributes:
        messages: Historial de mensajes de la conversación.
                  Usa add_messages para acumular mensajes automáticamente.
    """
    messages: Annotated[list, add_messages]
