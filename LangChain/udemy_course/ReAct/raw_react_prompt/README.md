# Raw ReAct Prompt (Notebook)

## Files

- `3_raw_react_prompt.ipynb`: Jupyter notebook version of the raw ReAct prompt agent.

## What This Demonstrates

- Raw prompt-driven agent behavior (no native tool binding in the chat call)
- Tool descriptions generated from Python signatures/docstrings
- Regex parsing of `Action` and `Action Input`
- Scratchpad replay across iterations
- Controlled observations via stop tokens

## Prerequisites

- Python 3.10+
- Ollama installed and running
- Model available locally: `qwen3:1.7b`

## Install Dependencies

```bash
pip install langchain langsmith ollama python-dotenv jupyter
```

## Pull the Model

```bash
ollama pull qwen3:1.7b
```

## Run

1. Open Jupyter in this directory.
2. Open `3_raw_react_prompt.ipynb`.
3. Run cells from top to bottom.
4. The final cell runs:
   `What is the price of a laptop after applying a gold discount?`

## Notes

- The parser expects the LLM to follow the exact ReAct text format.
- If output format drifts, regex parsing can fail.
- `MAX_ITERATIONS` and `MODEL` are configurable in the notebook.
