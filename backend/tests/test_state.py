from src.agents.state import ChatState


def test_chat_state_has_messages_field():
    """ChatState should have a messages field."""
    state: ChatState = {"messages": []}
    assert "messages" in state
    assert isinstance(state["messages"], list)
