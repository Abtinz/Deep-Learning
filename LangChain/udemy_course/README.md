# Udemy Course Workspace (LangChain)

This directory contains practical course exercises and refactors for building LLM applications with LangChain and LangGraph.

## Folders

- `hello_world/`: foundational prompt + context workflows
- `search-agent/`: search-enabled agent scaffold with Tavily
- `ReAct/`: tool-calling ReAct patterns (LangChain + raw approaches)
- `RAGs/`: retrieval projects and notebooks
  - `Medium_analyzer/`
  - `Tavily/`
  - `langchain Documentation Helper(agentic-rag)/`
- `langgraph/`: ReAct-style LangGraph agent with crawl/search tooling

## Environment

Most projects use `.env`-based configuration. Common variables:

- `OPENAI_API_KEY`
- `TAVILY_API_KEY`
- `LANGCHAIN_API_KEY`
- `LANGCHAIN_TRACING_V2`
- `LANGCHAIN_ENDPOINT`
- `LANGCHAIN_PROJECT`

## Setup Pattern (`uv`)

Most subprojects follow this flow:

```bash
cd <target-project>
uv sync
source .venv/bin/activate
python main.py
```

For `langgraph/`, use:

```bash
cd LangChain/udemy_course/langgraph
./setup.sh
```

## Purpose

The goal of this workspace is to keep each concept isolated and runnable:

- prompt engineering
- tool calling
- retrieval augmentation (RAG)
- agent loops and graph orchestration
