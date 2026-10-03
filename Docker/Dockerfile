FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.12.19 /uv /uvx /bin/
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 UV_PYTHON_DOWNLOADS=0 UV_LINK_MODE=copy PATH="/workspace/.venv/bin:$PATH"
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates git && rm -rf /var/lib/apt/lists/* && groupadd --gid 1000 vscode && useradd --uid 1000 --gid vscode --create-home --shell /bin/bash vscode
WORKDIR /workspace
COPY pyproject.toml README.md ./
COPY src/ ./src/
RUN uv sync --no-dev --no-cache && chown -R vscode:vscode /workspace
USER vscode
EXPOSE 8000
CMD ["uv","run","--no-sync","uvicorn","my_agent.api.main:app","--host","0.0.0.0","--port","8000","--reload"]
