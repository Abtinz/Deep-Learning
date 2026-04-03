# LangChain

This folder contains LangChain-based applications and course exercises, including prompt pipelines, ReAct agents, and search-enabled agents.

## What LangChain Means Here

- LangChain is used as an orchestration layer for prompts, models, tools, and multi-step agent workflows.
- The material compares framework-native abstractions vs lower-level/raw implementations.

## Core Concepts Implemented

- Prompt-template chaining.
- Tool calling with agent loops.
- ReAct-style reasoning and action/observation cycles.
- Structured agent responses with sources.
- Multi-provider model usage (OpenAI + Ollama).

## Projects In This Folder

- `Travel Scheduler/Travel_Scheduler_LLM.ipynb`
  - LLM-based travel planning notebook.
- `udemy_course/hello_world`
  - `main.py`, `prompt.py`, `knowledgebase.py`
  - Intro pipeline comparing OpenAI and Ollama chats.
- `udemy_course/ReAct`
  - `tool_calling/1_agent_loop_langchain_tool_calling.py`
  - `raw_tool_calling/raw_tool_calling.py`
  - `raw_react_prompt/3_raw_react_prompt.ipynb`
  - ReAct implementations at different abstraction levels.
- `udemy_course/search-agent/main.py`
  - Search agent with structured output schema and external search tool integration.

## Models and Technologies Referenced

- OpenAI: `gpt-5`, `gpt-3.5-turbo`
- Ollama models: `gemma3:270m`, `qwen3:1.7b`
- Tavily search integration
- LangSmith tracing

