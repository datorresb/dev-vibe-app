"""Integration tests for agent graph requiring Azure credentials."""

import pytest
from src.agents.agent import create_agent


@pytest.mark.integration
def test_create_agent_function_exists():
    """create_agent function should be available and working."""
    agent, memory = create_agent()
    assert agent is not None
    assert memory is not None


@pytest.mark.integration
def test_agent_has_nodes():
    """Agent graph should have agent and tools nodes."""
    agent, memory = create_agent()
    node_names = list(agent.nodes.keys())
    assert "agent" in node_names
    assert "tools" in node_names


@pytest.mark.integration
def test_agent_has_memory():
    """Agent should have memory checkpointer."""
    agent, memory = create_agent()
    assert hasattr(memory, 'put')
    assert hasattr(memory, 'get')
