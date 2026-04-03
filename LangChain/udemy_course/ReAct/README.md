# ReAct Agent Implementations

## Project Overview

ReAct Agent Implementations is a focused project in this repository that explores multi-step reasoning + tool-use loops at framework and raw SDK levels. The implementation is notebook/script oriented, so you can inspect each phase (setup, experimentation, and outputs) in a practical, reproducible workflow.

The project is designed as a learning-and-building artifact rather than just a final demo. That means the folder captures iterative reasoning, experimentation choices, and intermediate patterns that are useful for extending the work into larger systems.

## Project Files

- `main.py`
- `pyproject.toml`

## Technologies Used

The technical stack used here includes LangChain tool binding, Raw provider SDK patterns, LangSmith tracing, Python. These technologies were selected to keep the workflow modular: data/loading, model execution, and evaluation can each be changed independently without rewriting the whole project.

From an engineering perspective, this stack supports fast iteration and clear separation of concerns. It allows you to move between notebook exploration and script-style execution, which is useful when transitioning from prototyping to a more production-oriented layout.

## Models and Core Tools

The core model/tooling layer in this project is: `gpt-3.5-turbo` (LangChain tool_calling), `qwen3:1.7b` via Ollama (raw variants). This model/tool choice defines the project’s quality, speed, and behavior envelope, so most of the prompt/configuration decisions in the folder are tuned around it.

Conceptually, this layer is the engine of the project: it transforms raw inputs into task-specific outputs and determines what kind of reasoning or generation is possible. Understanding this layer deeply helps you decide where to tune parameters, where to add retrieval/tools, and where to switch to a different model family entirely.

## Requirements

- Python 3.10+
- langchain
- langsmith
- ollama
- python-dotenv
- OpenAI key for tool_calling path

## Running Steps

1. LangChain version: run `tool_calling/1_agent_loop_langchain_tool_calling.py`.
2. Raw SDK version: run `raw_tool_calling/raw_tool_calling.py`.
3. Prompt-only notebook: run `raw_react_prompt/3_raw_react_prompt.ipynb`.
