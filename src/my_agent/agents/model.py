"""Model adapter independent of the chosen inference service."""

from langchain_openai import ChatOpenAI

from my_agent.core.config import get_settings


def get_chat_model() -> ChatOpenAI:
    """Construct the configured OpenAI-compatible chat model."""
    settings = get_settings()
    return ChatOpenAI(
        model=settings.model_id,
        base_url=settings.openai_base_url,
        api_key=settings.openai_api_key,
    )
