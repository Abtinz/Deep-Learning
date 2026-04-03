# Raw ReAct Prompt Project

## Project Overview

Raw ReAct Prompt Project is a focused project in this repository that explores prompt-only ReAct pattern with regex parsing of action steps. The implementation is notebook/script oriented, so you can inspect each phase (setup, experimentation, and outputs) in a practical, reproducible workflow.

The project is designed as a learning-and-building artifact rather than just a final demo. That means the folder captures iterative reasoning, experimentation choices, and intermediate patterns that are useful for extending the work into larger systems.

## Project Files

- `3_raw_react_prompt.ipynb`

## Technologies Used

The technical stack used here includes Jupyter Notebook, Ollama SDK, Regex parsing, LangSmith tracing. These technologies were selected to keep the workflow modular: data/loading, model execution, and evaluation can each be changed independently without rewriting the whole project.

From an engineering perspective, this stack supports fast iteration and clear separation of concerns. It allows you to move between notebook exploration and script-style execution, which is useful when transitioning from prototyping to a more production-oriented layout.

## Models and Core Tools

The core model/tooling layer in this project is: Ollama `qwen3:1.7b`. This model/tool choice defines the project’s quality, speed, and behavior envelope, so most of the prompt/configuration decisions in the folder are tuned around it.

Conceptually, this layer is the engine of the project: it transforms raw inputs into task-specific outputs and determines what kind of reasoning or generation is possible. Understanding this layer deeply helps you decide where to tune parameters, where to add retrieval/tools, and where to switch to a different model family entirely.

## Requirements

- Python 3.10+
- jupyter
- ollama
- langsmith
- python-dotenv
- running Ollama server

## Running Steps

1. Open `3_raw_react_prompt.ipynb`.
2. Ensure Ollama is running and model is pulled.
3. Run notebook top-to-bottom.
