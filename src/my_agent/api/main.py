"""FastAPI entry point."""

from fastapi import FastAPI

app = FastAPI(title="My_Agent", version="0.1.0")


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    """Liveness probe; external dependency checks will be added separately."""
    return {"status": "ok"}
