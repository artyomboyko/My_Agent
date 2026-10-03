# Architecture

My_Agent starts as a modular monolith. Keep one API and one independently evolving
universal agent, while preserving explicit boundaries between features.

## Modules

- api: HTTP routes, request validation, and response schemas.
- core: configuration and common application primitives.
- agents: agent runtime, planning, tools, memory, and future subagent delegation.
- rag: document ingestion, retrieval, reranking, and Qdrant-backed memory.
- evaluation: benchmark adapters, experiment orchestration, and comparable metrics.
- infrastructure: PostgreSQL repositories and integrations with external services.

## Infrastructure

Docker Compose starts the FastAPI service, PostgreSQL, and Qdrant. Development uses
the same API service through the VS Code Dev Container, with the virtual environment
stored in a Docker volume. All published ports bind to localhost by default.

PostgreSQL will hold application state, run metadata, and experiment results.
Qdrant will hold retrieval indexes, not benchmark answers. Benchmark ground truth
must remain isolated from the agent and the retrieval corpus.

## Evolution

1. Add a minimal LangGraph-powered agent and a model-provider interface.
2. Add benchmark adapters and reproducible experiment records.
3. Implement baseline RAG, then agent-controlled retrieval.
4. Introduce DeepAgents and subagents where measured results justify them.
5. Add a task queue, isolated execution workers, and observability when required.

Do not put business logic in API handlers. Do not couple the universal agent
to a particular benchmark, model provider, or database implementation.
