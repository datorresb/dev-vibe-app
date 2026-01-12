"""
Chainlit app - UI para el chatbot conversacional.

Ejecutar con: chainlit run app.py
"""

import chainlit as cl
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

# Cargar variables de entorno
load_dotenv()

from src.agents import get_graph


@cl.on_chat_start
async def on_chat_start():
    """Inicializa la sesión de chat."""
    # Inicializar estado de la conversación
    cl.user_session.set("messages", [])

    await cl.Message(
        content="Hola! Soy un asistente conversacional powered by LangGraph + Azure GPT 5.1. ¿En qué puedo ayudarte?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    """Procesa cada mensaje del usuario."""
    # Obtener historial de mensajes
    messages = cl.user_session.get("messages", [])

    # Añadir mensaje del usuario
    messages.append(HumanMessage(content=message.content))

    # Invocar el grafo
    graph = get_graph()
    result = await cl.make_async(graph.invoke)({"messages": messages})

    # Obtener respuesta del asistente
    assistant_message = result["messages"][-1]

    # Actualizar historial
    messages.append(assistant_message)
    cl.user_session.set("messages", messages)

    # Enviar respuesta
    await cl.Message(content=assistant_message.content).send()


if __name__ == "__main__":
    # Para desarrollo local
    from chainlit.cli import run_chainlit
    run_chainlit(__file__)
