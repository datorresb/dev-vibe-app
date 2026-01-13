from src.agents.tools import web_fetch


def test_web_fetch_is_a_tool():
    """web_fetch should be a LangChain tool."""
    assert hasattr(web_fetch, "name")
    assert web_fetch.name == "web_fetch"


def test_web_fetch_has_description():
    """web_fetch should have a description for the LLM."""
    assert web_fetch.description
    assert "url" in web_fetch.description.lower()
