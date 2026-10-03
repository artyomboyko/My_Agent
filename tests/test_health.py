"""Smoke tests for the HTTP application."""

from fastapi.testclient import TestClient

from my_agent.api.main import app


def test_health() -> None:
    """Health should not depend on an LLM or running database."""
    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
