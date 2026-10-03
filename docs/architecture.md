# Architecture

My_Agent is a single universal agent with a modular core. Infrastructure
components can become independent services when there is a demonstrated need.

## Current components

- FastAPI backend: HTTP API, agent package, configuration, and model adapter.
- vLLM inference: optional Docker Compose profile with an OpenAI-compatible API.
- Dev Container: connects to the backend service from Docker/compose.yaml.

The agent does not depend on the local inference implementation. Its model
adapter uses the OpenAI-compatible API and can later point to a cloud model.

## Planned evolution

1. LangChain agent and basic tools.
2. LangGraph orchestration, state, and benchmark adapters.
3. Qdrant-backed RAG and agent-controlled retrieval.
4. DeepAgents, subagents, and richer planning.
5. Isolated execution, background workers, and benchmark environments.

PostgreSQL, Qdrant, and queue services will be added when needed. Benchmark
ground truth must stay inaccessible to the agent and its retrieval corpus.
