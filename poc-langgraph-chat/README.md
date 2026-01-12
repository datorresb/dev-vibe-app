# POC: LangGraph Conversational Chatbot

Chatbot conversacional usando LangGraph + Chainlit + Azure OpenAI GPT 5.1.

## Stack

- **LangGraph**: Backend conversacional con estado
- **Chainlit**: UI web para chat
- **Azure OpenAI**: GPT 5.1 con Managed Identity
- **UV**: Gestor de paquetes

## Setup

```bash
# Instalar dependencias con UV
uv sync

# Configurar Azure (local dev)
az login

# Copiar y editar variables de entorno
cp .env.example .env

# Ejecutar
uv run chainlit run app.py
```

## Estructura

```
poc-langgraph-chat/
├── app.py                    # Chainlit UI
├── src/
│   ├── __init__.py
│   └── agents/
│       ├── __init__.py       # Exports públicos
│       ├── state.py          # Definición de estados
│       ├── tools.py          # LLM y herramientas
│       └── graph.py          # Definición del grafo
├── pyproject.toml            # Dependencias
└── .env.example              # Config example
```

## Flujo

```
Usuario → Chainlit → LangGraph → Azure OpenAI → Respuesta
```
