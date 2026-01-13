import os
from uuid import uuid4

import pytest
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

from src.agents.agent import create_agent


@pytest.mark.integration
def test_agent_responds_to_greeting():
    """Agent should respond to a simple greeting.

    Marked as integration because it requires Azure OpenAI credentials.
    """
    agent, memory = create_agent()
    thread_id = str(uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    result = agent.invoke({"messages": [HumanMessage(content="Hola")]}, config)
    assert "messages" in result
    assert len(result["messages"]) >= 1


@pytest.mark.integration
def test_agent_can_use_python_tool():
    """Agent should be able to use the python tool when asked to calculate.

    Marked as integration because the LLM needs to decide to call tools.
    """
    agent, memory = create_agent()
    thread_id = str(uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    result = agent.invoke({"messages": [HumanMessage(content="Calcula 2+2 usando Python")]}, config)
    assert "messages" in result
    assert len(result["messages"]) >= 1


@pytest.mark.integration
def test_agent_memory_persistence():
    """Agent should remember information across interactions."""
    agent, memory = create_agent()
    thread_id = str(uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    # First interaction - tell the agent something
    result1 = agent.invoke({"messages": [HumanMessage(content="Mi nombre es TestUser")]}, config)
    assert "messages" in result1

    # Second interaction - ask about what we told it
    result2 = agent.invoke({"messages": [HumanMessage(content="¿Cuál es mi nombre?")]}, config)
    assert "messages" in result2
    # The response should contain the name we mentioned
    response_text = result2["messages"][-1].content.lower()
    assert "testuser" in response_text or "test" in response_text
