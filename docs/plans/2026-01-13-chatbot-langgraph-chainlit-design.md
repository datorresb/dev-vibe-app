# Chatbot Conversacional: LangGraph + Chainlit + Azure OpenAI

**Fecha:** 2026-01-13
**Propósito:** POC + Material educativo
**Audiencia:** Developers con experiencia en LLMs

## Objetivo

Crear un chatbot conversacional que demuestre:
- LangGraph para orquestación de agentes
- Chainlit como UI
- Azure OpenAI con Managed Identity (MSI)
- Tools: web fetch y ejecución de Python (pandas, matplotlib)

## Roadmap (Backlog)

| Fase | Feature | Descripción |
|------|---------|-------------|
| 1 | Grafo básico | Nodos, edges, estado. Fundamentos |
| 2 | Ciclos/condicionales | Lógica de agente (tool vs responder) |
| 3 | Checkpointing | Persistencia de conversaciones |
| 4 | Human-in-the-loop | Aprobación antes de ejecutar |

## Arquitectura

```
backend/
├── chainlit_app.py           # Entry point - Chainlit UI
├── src/
│   ├── __init__.py
│   └── agents/
│       ├── __init__.py       # Exports: graph, ChatState
│       ├── state.py          # TypedDict con historial
│       ├── tools.py          # web_fetch, run_python
│       └── graph.py          # LangGraph definition
├── pyproject.toml            # Dependencies (uv)
└── .env                      # Symlink a /.env (no duplicar)
```

## Implementación

### 1. State (`src/agents/state.py`)

```python
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import AnyMessage, add_messages

class ChatState(TypedDict):
    """Estado del agente conversacional."""
    messages: Annotated[list[AnyMessage], add_messages]
```

### 2. Tools (`src/agents/tools.py`)

```python
from langchain_core.tools import tool
import subprocess
import tempfile

@tool
def web_fetch(url: str) -> str:
    """Fetch content from a URL and return as text."""
    import httpx
    response = httpx.get(url, follow_redirects=True)
    return response.text[:10000]

@tool
def run_python(code: str) -> str:
    """Execute Python code and return output. Supports pandas, matplotlib."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        f.flush()
        result = subprocess.run(
            ['python', f.name],
            capture_output=True,
            text=True,
            timeout=30
        )
    return result.stdout + result.stderr
```

### 3. Graph (`src/agents/graph.py`)

```python
import os
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_openai import AzureChatOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

from .state import ChatState
from .tools import web_fetch, run_python

# Azure OpenAI con MSI
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
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
    last_message = state["messages"][-1]
    if last_message.tool_calls:
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

### 4. Chainlit App (`chainlit_app.py`)

```python
import chainlit as cl
from src.agents.graph import graph
from langchain_core.messages import HumanMessage

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("messages", [])

@cl.on_message
async def on_message(message: cl.Message):
    messages = cl.user_session.get("messages", [])
    messages.append(HumanMessage(content=message.content))

    result = await cl.make_async(graph.invoke)({"messages": messages})

    cl.user_session.set("messages", result["messages"])
    final_response = result["messages"][-1].content

    await cl.Message(content=final_response).send()
```

### 5. Dependencies (`pyproject.toml`)

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

## Flujo del Grafo

```
START → agent → (tiene tool_calls?)
                  ├─ sí → tools → agent (loop)
                  └─ no → END
```

## Configuración

Reusar variables del proyecto raíz:
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_OPENAI_CHAT_DEPLOYMENT`

```bash
# En backend/
ln -s ../.env .env
```

## Ejecución

```bash
cd backend
uv sync
chainlit run chainlit_app.py
```

## Verificación

1. Abrir http://localhost:8000
2. Probar conversación básica: "Hola, ¿cómo estás?"
3. Probar web_fetch: "Busca información sobre LangGraph en https://langchain-ai.github.io/langgraph/"
4. Probar run_python: "Crea un gráfico simple con matplotlib que muestre los números del 1 al 10"

## Decisiones Técnicas

| Decisión | Elección | Razón |
|----------|----------|-------|
| Arquitectura | Modular (src/agents/) | Testeable, reutilizable |
| Ejecución Python | Subprocess local | Simple para POC, Docker después |
| Auth Azure | MSI | Sin API keys en código |
| State | Solo messages | YAGNI - expandir en fases futuras |
