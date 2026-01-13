import httpx
from langchain_core.tools import tool


@tool
def web_fetch(url: str) -> str:
    """Fetch content from a URL and return as text. Use this to retrieve web pages."""
    response = httpx.get(url, follow_redirects=True, timeout=30)
    response.raise_for_status()
    return response.text[:10000]
