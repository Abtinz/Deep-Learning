# CopilotKit Capital Chatbot (Python + FastAPI + LangChain)

## Project Path
`ui/ux kits/copilotkit-capital-chatbot`

## What It Does
- Exposes a Python FastAPI backend for country-capital queries
- Uses LangChain `ChatOpenAI` to resolve capitals
- Registers a CopilotKit endpoint at `/copilotkit` when the `copilotkit` package is available
- Provides fallback endpoint at `/capital`

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI key:
   ```bash
   export OPENAI_API_KEY="your_key_here"
   ```

## Run Tests
```bash
pytest -q
```

## Run API Server
```bash
uvicorn app:app --host 0.0.0.0 --port 9000
```

## Endpoints
- `GET /health`
- `GET /copilotkit-status`
- `POST /capital`
- `POST /copilotkit` (available when CopilotKit imports successfully)

## Python Version Note
`copilotkit` currently may not install on Python 3.13+ in some environments. The app still runs with fallback endpoints and reports CopilotKit status via `/copilotkit-status`.
