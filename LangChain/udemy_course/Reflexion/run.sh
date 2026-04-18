#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

# Ignore unrelated active virtualenvs from sibling projects.
if [[ "${VIRTUAL_ENV:-}" != "" && "${VIRTUAL_ENV}" != "${PROJECT_DIR}/.venv" ]]; then
  unset VIRTUAL_ENV
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required but not installed. Run ./setup.sh first."
  exit 1
fi

exec uv run streamlit run streamlit_app.py "$@"
