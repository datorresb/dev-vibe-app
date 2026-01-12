"""
Tools and LLM configuration for the agent.

Configura aquí el cliente de Azure OpenAI y cualquier herramienta adicional.
"""

import os
from functools import lru_cache

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain_openai import AzureChatOpenAI


@lru_cache(maxsize=1)
def get_token_provider():
    """
    Obtiene el token provider para Azure Managed Identity.

    Usa lru_cache para reutilizar el provider.
    """
    return get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default"
    )


def create_llm(
    temperature: float = 0.7,
    streaming: bool = False,
) -> AzureChatOpenAI:
    """
    Crea el cliente de Azure OpenAI con Managed Identity.

    Args:
        temperature: Creatividad del modelo (0.0 - 1.0)
        streaming: Habilitar streaming de respuestas

    Returns:
        Cliente AzureChatOpenAI configurado

    Requires env vars:
        - AZURE_OPENAI_ENDPOINT
        - AZURE_OPENAI_CHAT_DEPLOYMENT
        - AZURE_OPENAI_API_VERSION
    """
    return AzureChatOpenAI(
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        azure_ad_token_provider=get_token_provider(),
        temperature=temperature,
        streaming=streaming,
    )


# Herramientas adicionales se pueden definir aquí
# Ejemplo:
# from langchain_core.tools import tool
#
# @tool
# def search_web(query: str) -> str:
#     """Busca información en la web."""
#     pass
