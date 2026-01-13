from src.agents.tools import run_python, web_fetch


def test_web_fetch_is_a_tool():
    """web_fetch should be a LangChain tool."""
    assert hasattr(web_fetch, "name")
    assert web_fetch.name == "web_fetch"


def test_web_fetch_has_description():
    """web_fetch should have a description for the LLM."""
    assert web_fetch.description
    assert "url" in web_fetch.description.lower()


def test_run_python_is_a_tool():
    """run_python should be a LangChain tool."""
    assert hasattr(run_python, "name")
    assert run_python.name == "run_python"


def test_run_python_executes_code():
    """run_python should execute Python code and return output."""
    result = run_python.invoke({"code": "print('hello')"})
    assert "hello" in result
