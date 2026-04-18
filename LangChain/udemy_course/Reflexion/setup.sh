#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

# If another project's virtualenv is active, ignore it for this project setup.
if [[ "${VIRTUAL_ENV:-}" != "" && "${VIRTUAL_ENV}" != "${PROJECT_DIR}/.venv" ]]; then
  unset VIRTUAL_ENV
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "uv not found. Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi

uv sync

if [[ ! -f .env && -f .env.example ]]; then
  cp .env.example .env
  echo "Created .env from .env.example. Add your API keys before running."
fi

if [[ "${1:-}" == "run" ]]; then
  if [[ -f main.py ]]; then
    uv run python main.py
  else
    echo "No main.py found yet. Create it, then run: ./setup.sh run"
  fi
else
  echo "Setup complete."
  echo "Next: ./setup.sh run"
fi
