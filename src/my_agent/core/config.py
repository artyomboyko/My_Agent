"""Centralized model configuration."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for local development and OpenAI-compatible inference."""

    model_config = SettingsConfigDict(extra="ignore")

    openai_base_url: str = "http://localhost:8001/v1"
    openai_api_key: str = "local-development"
    model_id: str = "Qwen/Qwen3-0.6B"


@lru_cache
def get_settings() -> Settings:
    """Reuse validated settings across components."""
    return Settings()
