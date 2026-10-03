"""Centralized application settings."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for local development and containerized deployment."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    database_url: str = (
        "postgresql+asyncpg://my_agent:change_me_local@localhost:5432/my_agent"
    )
    qdrant_url: str = "http://localhost:6333"


@lru_cache
def get_settings() -> Settings:
    """Reuse validated settings across application components."""
    return Settings()
