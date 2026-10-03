# My_Agent

A universal AI agent.

My_Agent evolves incrementally as we add tools, planning, memory, RAG,
subagents, and reproducible benchmarks.

## Initial stack

Python 3.12, FastAPI, LangChain, uv, optional local vLLM inference,
Docker Compose, Dev Containers, pytest, and Ruff.

## Start development

Install Docker with Compose and clone this repository. From the project root:

~~~sh
cp Docker/.env.example Docker/.env
docker compose --env-file Docker/.env -f Docker/compose.yaml up --build -d backend
~~~

Backend health: http://localhost:8000/health
API documentation: http://localhost:8000/docs

To start the optional local inference service, use a supported NVIDIA GPU
and a configured NVIDIA Container Toolkit:

~~~sh
docker compose --env-file Docker/.env -f Docker/compose.yaml --profile local-inference up --build -d
~~~

Inference API: http://localhost:8001/v1

The default Qwen/Qwen3-0.6B is a lightweight connectivity test model, not a
recommended agent benchmark model. Select an agent-capable model based
on available VRAM. Model weights are cached in a Docker volume.

For VS Code development, select "Dev Containers: Reopen in Container".
VS Code opens the backend from Docker/compose.yaml and runs uv sync
to install development dependencies.

Inside the Dev Container:

~~~sh
uv run --no-sync pytest
uv run --no-sync ruff check .
uv run --no-sync ruff format --check .
~~~

The first successful uv sync generates uv.lock; commit that lock file for
reproducible installations and switch image builds to uv sync --locked.

This first version contains the backend health endpoint and model adapter,
not a complete agent. PostgreSQL and Qdrant are deliberately deferred.
See docs/architecture.md for the module boundaries and roadmap.

## License

PolyForm Noncommercial License 1.0.0. Commercial use is governed by
the license terms and, where required, a separate commercial license.
