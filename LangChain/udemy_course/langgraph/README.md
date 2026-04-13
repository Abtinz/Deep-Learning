# LangGraph ReAct Agent

A focused LangGraph project for building a ReAct-style tool-using agent with LangChain, Tavily search/crawl, and safe loop controls.

## Highlights

- LangGraph state-machine flow (`agent_reason -> act -> agent_reason`)
- Tool-enabled LLM with:
  - `TavilySearch`
  - `tavily_crawl`
  - `save_results`
  - `triple`
- Crawl quality guardrails in the system prompt
- Crawl depth normalization (`extract_depth` supports legacy int input)
- Loop safety via recursion and message-count limits

## Project Structure

- `main.py`: graph wiring, routing, and runnable entrypoint
- `nodes.py`: reasoning node + system prompt policy
- `react.py`: model/tool definitions and Tavily helper utilities
- `setup.sh`: one-command setup and run (`uv sync`, activate, execute)
- `.env.example`: required environment variables
- `crawled/`: persisted crawl outputs (created at runtime)

## Requirements

- Python 3.11+
- `uv`
- API keys:
  - `OPENAI_API_KEY`
  - `TAVILY_API_KEY`
  - optional LangSmith tracing keys (`LANGCHAIN_*`)

## Quick Start

```bash
cd LangChain/udemy_course/langgraph
cp .env.example .env
# add your real keys to .env
./setup.sh
```

## Manual Run

```bash
cd LangChain/udemy_course/langgraph
uv sync
source .venv/bin/activate
python main.py
```

## Notes

- If a crawl result is weak/invalid, the agent is instructed to search again and try a better source.
- The graph has bounded retries to avoid infinite tool loops.
