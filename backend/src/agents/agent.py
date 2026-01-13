"""LangGraph chatbot agent with Azure OpenAI and memory persistence."""

from __future__ import annotations

import os
from typing import Literal

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import SystemMessage
from langchain_openai import AzureChatOpenAI
from langgraph.graph import END, StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver

from .state import ChatState
from .tools import run_python, web_fetch


SYSTEM_PROMPT = """You are a helpful AI assistant that can execute Python code and fetch web content.

AVAILABLE TOOLS:
• run_python(code) - Execute Python code with pandas and matplotlib support
• web_fetch(url) - Fetch and return content from web URLs

You can help with:
- Data analysis and visualization
- Web scraping and research
- General programming questions
- Mathematical calculations

When executing code, be mindful of security and resource usage. Always explain what you're doing before running code.
"""


def _required_env(name: str) -> str:
    """Get required environment variable or raise error."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def _create_azure_llm() -> AzureChatOpenAI:
    """Create Azure OpenAI LLM with MSI authentication."""
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default",
    )

    return AzureChatOpenAI(
        azure_deployment=_required_env("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        azure_endpoint=_required_env("AZURE_OPENAI_ENDPOINT"),
        api_version=_required_env("AZURE_OPENAI_API_VERSION"),
        azure_ad_token_provider=token_provider,
    )


def create_agent(
    llm: BaseChatModel | None = None,
    verbose: bool = False,
) -> tuple[CompiledStateGraph, MemorySaver]:
    """
    Create a LangGraph chatbot agent with memory persistence.

    Args:
        llm: Language model to use (defaults to Azure OpenAI)
        verbose: Print debug information

    Returns:
        Tuple of (compiled graph, memory checkpointer)
    """
    if llm is None:
        llm = _create_azure_llm()

    tools = [web_fetch, run_python]
    llm_with_tools = llm.bind_tools(tools)
    memory = MemorySaver()

    def should_continue(state: ChatState) -> Literal["tools", "__end__"]:
        """Decide whether to continue with tools or end."""
        last_message = state["messages"][-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        return END

    def agent_node(state: ChatState) -> dict:
        """Main agent node that processes messages and decides on actions."""
        if verbose:
            print(f"Agent processing {len(state['messages'])} messages...")

        # Add system message for context
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
        response = llm_with_tools.invoke(messages)

        if verbose and hasattr(response, "tool_calls") and response.tool_calls:
            tool_names = [tc.get("name", "unknown") for tc in response.tool_calls]
            print(f"Agent calling tools: {', '.join(tool_names)}")

        return {"messages": [response]}

    # Build the graph
    workflow = StateGraph(ChatState)
    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", ToolNode(tools))

    workflow.set_entry_point("agent")
    workflow.add_conditional_edges("agent", should_continue, {
        "tools": "tools",
        "__end__": END
    })
    workflow.add_edge("tools", "agent")

    graph = workflow.compile(checkpointer=memory)

    if verbose:
        print("Chatbot agent ready!")

    return graph, memory


def visualize_graph(graph: CompiledStateGraph) -> bytes | None:
    """Generate graph visualization as PNG bytes (requires graphviz)."""
    try:
        return graph.get_graph().draw_mermaid_png()
    except Exception as e:
        print(f"Visualization failed: {e}")
        return None
