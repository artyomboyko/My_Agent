# My_Agent

A universal AI agent.

My_Agent is developed incrementally as a single modular agent. Its capabilities,
architecture, and benchmark integrations will evolve over time.

## Stack

- Python 3.12, FastAPI, Pydantic, uv
- LangChain, LangGraph, DeepAgents
- PostgreSQL, SQLAlchemy, Qdrant
- Docker Compose and VS Code Dev Containers
- pytest and Ruff

## Quick start

Install Docker with the Compose plugin and clone this repository. Then run:

~~~sh
cp .env.example .env
docker compose up --build
~~~

The API is available at http://localhost:8000/docs and the liveness endpoint
at http://localhost:8000/health. Qdrant is available on localhost:6333.

The API starts with a health endpoint and an architectural skeleton. Agent
execution, document ingestion, and benchmark runners will be implemented
incrementally; they are not active HTTP endpoints yet.

## Development

Open the repository in VS Code with the Dev Containers extension and run
"Dev Containers: Reopen in Container". VS Code will attach to the same API
service defined in compose.yaml, and uv will install the development tools.

Run tests and linting from the container terminal:

~~~sh
uv run --no-sync pytest
uv run --no-sync ruff check .
uv run --no-sync ruff format --check .
~~~

The first uv sync creates uv.lock. Commit the generated lockfile after a
successful dependency resolution to make future builds reproducible. Once
uv.lock is committed, image builds can be changed to use uv sync --locked.

To stop the local stack:

~~~sh
docker compose down
~~~

Database and Qdrant data are stored in named Docker volumes; docker compose
down --volumes also deletes those local development volumes.

See docs/architecture.md for module boundaries and the planned evolution.

## License

PolyForm Noncommercial License 1.0.0. Commercial use is governed by the
license terms and, where required, a separate commercial license.
