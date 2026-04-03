# LangChain Hello World

## Project Overview

LangChain Hello World is a focused project in this repository that explores introductory chain composition with shared prompt/context across providers. The implementation is notebook/script oriented, so you can inspect each phase (setup, experimentation, and outputs) in a practical, reproducible workflow.

The project is designed as a learning-and-building artifact rather than just a final demo. That means the folder captures iterative reasoning, experimentation choices, and intermediate patterns that are useful for extending the work into larger systems.

## Project Files

- `knowledgebase.py`
- `main.py`
- `prompt.py`
- `pyproject.toml`

## Technologies Used

The technical stack used here includes LangChain, langchain-openai, langchain-ollama, dotenv. These technologies were selected to keep the workflow modular: data/loading, model execution, and evaluation can each be changed independently without rewriting the whole project.

From an engineering perspective, this stack supports fast iteration and clear separation of concerns. It allows you to move between notebook exploration and script-style execution, which is useful when transitioning from prototyping to a more production-oriented layout.

## Models and Core Tools

The core model/tooling layer in this project is: OpenAI `gpt-5`, Ollama `gemma3:270m`. This model/tool choice defines the project’s quality, speed, and behavior envelope, so most of the prompt/configuration decisions in the folder are tuned around it.

Conceptually, this layer is the engine of the project: it transforms raw inputs into task-specific outputs and determines what kind of reasoning or generation is possible. Understanding this layer deeply helps you decide where to tune parameters, where to add retrieval/tools, and where to switch to a different model family entirely.

## Requirements

- Python 3.10+
- langchain
- langchain-openai
- langchain-ollama
- python-dotenv
- OPENAI_API_KEY
- Ollama (for local model path)

## Running Steps

1. Set `.env` with required API keys.
2. Install deps from `pyproject.toml`.
3. Run `python main.py`.
