"""
LangGraph definition for the conversational agent.

Define aquí la estructura del grafo y sus nodos.
"""

from langgraph.graph import StateGraph, START, END

from .state import ConversationState
from .tools import create_llm


def create_chatbot_node(llm):
    """
    Crea el nodo principal del chatbot.

    Args:
        llm: Cliente de LLM a usar

    Returns:
        Función del nodo que procesa mensajes
    """
    def chatbot(state: ConversationState) -> ConversationState:
        """Procesa el mensaje y genera respuesta."""
        response = llm.invoke(state["messages"])
        return {"messages": [response]}

    return chatbot


def build_graph() -> StateGraph:
    """
    Construye el grafo conversacional.

    Estructura:
        START -> chatbot -> END

    Returns:
        Grafo compilado listo para usar
    """
    # Crear LLM
    llm = create_llm()

    # Crear nodos
    chatbot_node = create_chatbot_node(llm)

    # Construir grafo
    graph_builder = StateGraph(ConversationState)

    # Añadir nodos
    graph_builder.add_node("chatbot", chatbot_node)

    # Definir flujo
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    return graph_builder.compile()


# Singleton del grafo compilado
_graph = None


def get_graph():
    """
    Obtiene el grafo compilado (singleton).

    Returns:
        Grafo LangGraph compilado
    """
    global _graph
    if _graph is None:
        _graph = build_graph()
    return _graph
