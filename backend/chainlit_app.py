"""Chainlit app using evolved LangGraph agent with memory persistence."""

import os
from uuid import uuid4

import chainlit as cl
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

from src.agents.agent import create_agent


# Global agent and memory instances
_agent, _memory = create_agent(verbose=True)


@cl.on_chat_start
async def on_chat_start():
    """Initialize session with persistent memory."""
    # Create unique thread ID for this conversation
    thread_id = str(uuid4())
    cl.user_session.set("thread_id", thread_id)

    # Welcome message
    await cl.Message(
        content="¡Hola! Soy tu asistente AI con capacidades de programación Python y búsqueda web. "
                "Tengo memoria persistente, así que recordaré nuestra conversación. ¿En qué puedo ayudarte?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    """Process user message through LangGraph agent with persistent memory."""
    thread_id = cl.user_session.get("thread_id")
    config = {"configurable": {"thread_id": thread_id}}

    # Create human message
    input_data = {"messages": [HumanMessage(content=message.content)]}

    # Process through agent with memory
    result = await cl.make_async(_agent.invoke)(input_data, config)

    # Send response
    final_response = result["messages"][-1].content
    await cl.Message(content=final_response).send()


if __name__ == "__main__":
    cl.run()
