# LangGraph

## Project Overview

This folder is the initial LangGraph scaffold inside `LangChain/udemy_course`, aligned with the referenced course-style setup and adapted to `uv` tooling.

## Project Files

- `main.py`
- `nodes.py`
- `react.py`
- `pyproject.toml`
- `.env.example`

## Environment Variables

Set the following values in a local `.env` file:

- `OPENAI_API_KEY`
- `LANGCHAIN_API_KEY`
- `LANGCHAIN_TRACING_V2=true`
- `LANGCHAIN_ENDPOINT=https://api.smith.langchain.com`
- `LANGCHAIN_PROJECT=ReAct Function Calling`
- `TAVILY_API_KEY`

## Setup (uv)

1. `cd LangChain/udemy_course/langgraph`
2. `uv sync`
3. `cp .env.example .env` and fill in your real keys
4. `uv run python main.py`
