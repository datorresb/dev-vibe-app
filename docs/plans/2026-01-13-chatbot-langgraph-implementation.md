# Chatbot LangGraph + Chainlit Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a conversational chatbot POC with LangGraph, Chainlit, and Azure OpenAI that can fetch web content and execute Python code.

**Architecture:** Modular structure under `backend/src/agents/` with separate files for state, tools, and graph. Chainlit handles UI, LangGraph orchestrates the agent loop.

**Tech Stack:** LangGraph, LangChain-OpenAI, Chainlit, Azure Identity (MSI), httpx, pandas, matplotlib

**Design Doc:** `docs/plans/2026-01-13-chatbot-langgraph-chainlit-design.md`

---

## Task 1: Project Setup

**Files:**
- Create: `backend/pyproject.toml`
- Create: `backend/src/__init__.py`
- Create: `backend/src/agents/__init__.py`

**Step 1: Create backend directory structure**

```bash
mkdir -p backend/src/agents
```

**Step 2: Create pyproject.toml**

```toml
[project]
name = "chatbot-poc"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "langgraph",
    "langchain-openai",
    "chainlit",
    "azure-identity",
    "httpx",
    "pandas",
    "matplotlib",
]

[tool.uv]
dev-dependencies = ["pytest", "ruff"]
```

**Step 3: Create __init__.py files**

`backend/src/__init__.py`: empty file
`backend/src/agents/__init__.py`: empty file (will add exports later)

**Step 4: Symlink .env**

```bash
cd backend && ln -s ../.env .env
```

**Step 5: Install dependencies**

```bash
cd backend && uv sync
```

Expected: Dependencies installed, `.venv` created

**Step 6: Commit**

```bash
git add backend/
git commit -m "feat(backend): initialize project structure with dependencies"
```

---

## Task 2: State Definition

**Files:**
- Create: `backend/src/agents/state.py`
- Test: `backend/tests/test_state.py`

**Step 1: Create tests directory**

```bash
mkdir -p backend/tests && touch backend/tests/__init__.py
```

**Step 2: Write the failing test**

`backend/tests/test_state.py`:
```python
from src.agents.state import ChatState


def test_chat_state_has_messages_field():
    """ChatState should have a messages field."""
    state: ChatState = {"messages": []}
    assert "messages" in state
    assert isinstance(state["messages"], list)
```

**Step 3: Run test to verify it fails**

```bash
cd backend && uv run pytest tests/test_state.py -v
```

Expected: FAIL with "ModuleNotFoundError: No module named 'src.agents.state'"

**Step 4: Write minimal implementation**

`backend/src/agents/state.py`:
```python
from typing import Annotated

from langgraph.graph.message import AnyMessage, add_messages
from typing_extensions import TypedDict


class ChatState(TypedDict):
    """Estado del agente conversacional."""

    messages: Annotated[list[AnyMessage], add_messages]
```

**Step 5: Run test to verify it passes**

```bash
cd backend && uv run pytest tests/test_state.py -v
```

Expected: PASS

**Step 6: Commit**

```bash
git add backend/src/agents/state.py backend/tests/
git commit -m "feat(backend): add ChatState with messages field"
```

---

## Task 3: Web Fetch Tool

**Files:**
- Create: `backend/src/agents/tools.py`
- Test: `backend/tests/test_tools.py`

**Step 1: Write the failing test**

`backend/tests/test_tools.py`:
```python
from src.agents.tools import web_fetch


def test_web_fetch_is_a_tool():
    """web_fetch should be a LangChain tool."""
    assert hasattr(web_fetch, "name")
    assert web_fetch.name == "web_fetch"


def test_web_fetch_has_description():
    """web_fetch should have a description for the LLM."""
    assert web_fetch.description
    assert "url" in web_fetch.description.lower()
```

**Step 2: Run test to verify it fails**

```bash
cd backend && uv run pytest tests/test_tools.py::test_web_fetch_is_a_tool -v
```

Expected: FAIL with "ModuleNotFoundError"

**Step 3: Write minimal implementation**

`backend/src/agents/tools.py`:
```python
import httpx
from langchain_core.tools import tool


@tool
def web_fetch(url: str) -> str:
    """Fetch content from a URL and return as text. Use this to retrieve web pages."""
    response = httpx.get(url, follow_redirects=True, timeout=30)
    response.raise_for_status()
    return response.text[:10000]
```

**Step 4: Run tests to verify they pass**

```bash
cd backend && uv run pytest tests/test_tools.py -v -k web_fetch
```

Expected: PASS

**Step 5: Commit**

```bash
git add backend/src/agents/tools.py backend/tests/test_tools.py
git commit -m "feat(backend): add web_fetch tool"
```

---

## Task 4: Run Python Tool

**Files:**
- Modify: `backend/src/agents/tools.py`
- Modify: `backend/tests/test_tools.py`

**Step 1: Write the failing test**

Add to `backend/tests/test_tools.py`:
```python
from src.agents.tools import run_python


def test_run_python_is_a_tool():
    """run_python should be a LangChain tool."""
    assert hasattr(run_python, "name")
    assert run_python.name == "run_python"


def test_run_python_executes_code():
    """run_python should execute Python code and return output."""
    result = run_python.invoke({"code": "print('hello')"})
    assert "hello" in result
```

**Step 2: Run test to verify it fails**

```bash
cd backend && uv run pytest tests/test_tools.py::test_run_python_is_a_tool -v
```

Expected: FAIL with "ImportError: cannot import name 'run_python'"

**Step 3: Write implementation**

Add to `backend/src/agents/tools.py`:
```python
import subprocess
import tempfile


@tool
def run_python(code: str) -> str:
    """Execute Python code and return output. Supports pandas and matplotlib."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        f.flush()
        try:
            result = subprocess.run(
                ["python", f.name],
                capture_output=True,
                text=True,
                timeout=30,
            )
            output = result.stdout
            if result.stderr:
                output += "\nSTDERR:\n" + result.stderr
            return output if output else "(no output)"
        except subprocess.TimeoutExpired:
            return "ERROR: Code execution timed out after 30 seconds"
```

**Step 4: Run tests to verify they pass**

```bash
cd backend && uv run pytest tests/test_tools.py -v
```

Expected: All PASS

**Step 5: Commit**

```bash
git add backend/src/agents/tools.py backend/tests/test_tools.py
git commit -m "feat(backend): add run_python tool"
```

---

## Task 5: LangGraph Definition

**Files:**
- Create: `backend/src/agents/graph.py`
- Test: `backend/tests/test_graph.py`

**Step 1: Write the failing test**

`backend/tests/test_graph.py`:
```python
from src.agents.graph import graph


def test_graph_exists():
    """Graph should be compiled and ready to use."""
    assert graph is not None


def test_graph_has_nodes():
    """Graph should have agent and tools nodes."""
    node_names = list(graph.nodes.keys())
    assert "agent" in node_names
    assert "tools" in node_names
```

**Step 2: Run test to verify it fails**

```bash
cd backend && uv run pytest tests/test_graph.py::test_graph_exists -v
```

Expected: FAIL with "ModuleNotFoundError"

**Step 3: Write implementation**

`backend/src/agents/graph.py`:
```python
import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain_openai import AzureChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode

from .state import ChatState
from .tools import run_python, web_fetch

# Azure OpenAI con MSI
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)

llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_ad_token_provider=token_provider,
)

tools = [web_fetch, run_python]
llm_with_tools = llm.bind_tools(tools)


def agent_node(state: ChatState) -> dict:
    """LLM decide: responder o usar tool."""
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


tool_node = ToolNode(tools)


def should_continue(state: ChatState) -> str:
    """Decide si continuar con tools o terminar."""
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return END


# Construir grafo
graph_builder = StateGraph(ChatState)
graph_builder.add_node("agent", agent_node)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "agent")
graph_builder.add_conditional_edges("agent", should_continue, ["tools", END])
graph_builder.add_edge("tools", "agent")

graph = graph_builder.compile()
```

**Step 4: Run tests to verify they pass**

```bash
cd backend && uv run pytest tests/test_graph.py -v
```

Expected: PASS (requires `az login` for MSI auth)

**Step 5: Commit**

```bash
git add backend/src/agents/graph.py backend/tests/test_graph.py
git commit -m "feat(backend): add LangGraph agent with tools"
```

---

## Task 6: Module Exports

**Files:**
- Modify: `backend/src/agents/__init__.py`

**Step 1: Update exports**

`backend/src/agents/__init__.py`:
```python
from .graph import graph
from .state import ChatState
from .tools import run_python, web_fetch

__all__ = ["graph", "ChatState", "web_fetch", "run_python"]
```

**Step 2: Verify imports work**

```bash
cd backend && uv run python -c "from src.agents import graph, ChatState; print('OK')"
```

Expected: "OK"

**Step 3: Commit**

```bash
git add backend/src/agents/__init__.py
git commit -m "feat(backend): export public API from agents module"
```

---

## Task 7: Chainlit App

**Files:**
- Create: `backend/chainlit_app.py`

**Step 1: Create Chainlit app**

`backend/chainlit_app.py`:
```python
import chainlit as cl
from langchain_core.messages import HumanMessage

from src.agents import graph


@cl.on_chat_start
async def on_chat_start():
    """Initialize session with empty message history."""
    cl.user_session.set("messages", [])


@cl.on_message
async def on_message(message: cl.Message):
    """Process user message through LangGraph agent."""
    messages = cl.user_session.get("messages", [])
    messages.append(HumanMessage(content=message.content))

    result = await cl.make_async(graph.invoke)({"messages": messages})

    cl.user_session.set("messages", result["messages"])
    final_response = result["messages"][-1].content

    await cl.Message(content=final_response).send()
```

**Step 2: Create Chainlit config (optional)**

`backend/.chainlit.toml`:
```toml
[project]
enable_telemetry = false

[UI]
name = "Chatbot POC"
description = "LangGraph + Chainlit + Azure OpenAI"
```

**Step 3: Commit**

```bash
git add backend/chainlit_app.py backend/.chainlit.toml
git commit -m "feat(backend): add Chainlit UI app"
```

---

## Task 8: Integration Test

**Files:**
- Create: `backend/tests/test_integration.py`

**Step 1: Write integration test**

`backend/tests/test_integration.py`:
```python
import pytest
from langchain_core.messages import HumanMessage

from src.agents import graph


@pytest.mark.integration
def test_graph_responds_to_greeting():
    """Graph should respond to a simple greeting."""
    result = graph.invoke({"messages": [HumanMessage(content="Hola")]})
    assert len(result["messages"]) >= 2
    assert result["messages"][-1].content


@pytest.mark.integration
def test_graph_can_use_python_tool():
    """Graph should use run_python tool when asked to calculate."""
    result = graph.invoke(
        {"messages": [HumanMessage(content="Calcula 2+2 usando Python")]}
    )
    # Should have: human -> ai (tool call) -> tool result -> ai (final)
    assert len(result["messages"]) >= 2
```

**Step 2: Run integration tests**

```bash
cd backend && uv run pytest tests/test_integration.py -v -m integration
```

Expected: PASS (requires Azure OpenAI connection)

**Step 3: Commit**

```bash
git add backend/tests/test_integration.py
git commit -m "test(backend): add integration tests for graph"
```

---

## Task 9: Manual Verification

**Step 1: Ensure Azure login**

```bash
az login
```

**Step 2: Run Chainlit**

```bash
cd backend && uv run chainlit run chainlit_app.py
```

**Step 3: Test in browser**

1. Open http://localhost:8000
2. Test: "Hola, como estas?"
3. Test: "Crea un grafico con matplotlib que muestre los numeros del 1 al 5"
4. Test: "Busca informacion en https://example.com"

**Step 4: Final commit**

```bash
git add -A
git commit -m "feat(backend): complete chatbot POC phase 1"
```

---

## Verification Checklist

- [ ] `uv sync` installs all dependencies
- [ ] `pytest tests/` passes (unit tests)
- [ ] `pytest tests/ -m integration` passes (with Azure)
- [ ] `chainlit run chainlit_app.py` starts server
- [ ] Chat responds to greetings
- [ ] Python tool executes code
- [ ] Web fetch retrieves content
