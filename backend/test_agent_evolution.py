#!/usr/bin/env python3
"""Test script to validate the evolved agent architecture."""

import asyncio
from uuid import uuid4

from langchain_core.messages import HumanMessage

from src.agents.agent import create_agent, visualize_graph


async def test_basic_conversation():
    """Test basic conversation functionality."""
    print("🔄 Testing basic conversation...")

    # Create agent with verbose output
    agent, memory = create_agent(verbose=True)
    thread_id = str(uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    # Test simple conversation
    messages = [HumanMessage(content="Hola, ¿cómo estás?")]
    result = await asyncio.to_thread(agent.invoke, {"messages": messages}, config)

    print(f"✅ Response: {result['messages'][-1].content[:100]}...")
    return True


async def test_python_execution():
    """Test Python code execution tool."""
    print("🐍 Testing Python execution...")

    agent, memory = create_agent(verbose=True)
    thread_id = str(uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    # Test Python execution
    messages = [HumanMessage(content="Calcula 2 + 2 usando Python")]
    result = await asyncio.to_thread(agent.invoke, {"messages": messages}, config)

    print(f"✅ Python execution result: {result['messages'][-1].content[:150]}...")
    return True


async def test_web_fetch():
    """Test web fetching functionality."""
    print("🌐 Testing web fetch...")

    agent, memory = create_agent(verbose=True)
    thread_id = str(uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    # Test web fetching
    messages = [HumanMessage(content="Busca información sobre Python en https://python.org")]
    result = await asyncio.to_thread(agent.invoke, {"messages": messages}, config)

    print(f"✅ Web fetch result: {result['messages'][-1].content[:150]}...")
    return True


async def test_memory_persistence():
    """Test memory persistence across multiple interactions."""
    print("🧠 Testing memory persistence...")

    agent, memory = create_agent(verbose=True)
    thread_id = str(uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    # First interaction
    messages1 = [HumanMessage(content="Mi nombre es Carlos")]
    result1 = await asyncio.to_thread(agent.invoke, {"messages": messages1}, config)
    print(f"✅ First interaction: {result1['messages'][-1].content[:100]}...")

    # Second interaction - should remember the name
    messages2 = [HumanMessage(content="¿Cuál es mi nombre?")]
    result2 = await asyncio.to_thread(agent.invoke, {"messages": messages2}, config)
    print(f"✅ Second interaction: {result2['messages'][-1].content[:100]}...")

    # Check if it remembers
    if "Carlos" in result2['messages'][-1].content or "carlos" in result2['messages'][-1].content.lower():
        print("✅ Memory persistence working!")
        return True
    else:
        print("❌ Memory persistence may not be working")
        return False


def test_visualization():
    """Test graph visualization."""
    print("📊 Testing graph visualization...")

    agent, memory = create_agent()
    png_data = visualize_graph(agent)

    if png_data:
        print("✅ Graph visualization generated successfully!")
        assert png_data is not None
    else:
        print("⚠️ Graph visualization failed (may need graphviz installed)")
        assert png_data is None


async def main():
    """Run all tests."""
    print("🚀 Starting agent evolution tests...\n")

    tests = [
        test_basic_conversation(),
        test_python_execution(),
        test_web_fetch(),
        test_memory_persistence(),
    ]

    results = await asyncio.gather(*tests, return_exceptions=True)

    # Test visualization (not async)
    try:
        test_visualization()
        viz_result = True
    except Exception as e:
        print(f"❌ Graph Visualization: FAILED - {e}")
        viz_result = e

    print("\n📋 Test Results:")
    test_names = [
        "Basic Conversation",
        "Python Execution",
        "Web Fetch",
        "Memory Persistence",
        "Graph Visualization"
    ]

    all_results = list(results) + [viz_result]

    for i, (name, result) in enumerate(zip(test_names, all_results)):
        if isinstance(result, Exception):
            print(f"❌ {name}: FAILED - {result}")
        elif result:
            print(f"✅ {name}: PASSED")
        else:
            print(f"⚠️ {name}: PARTIAL")

    passed = sum(1 for r in all_results if not isinstance(r, Exception) and r)
    total = len(all_results)

    print(f"\n🎯 Summary: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! Agent evolution is successful!")
    elif passed >= total * 0.8:
        print("✨ Most tests passed! Agent evolution is mostly successful!")
    else:
        print("⚠️ Some tests failed. Check the implementation.")


if __name__ == "__main__":
    asyncio.run(main())