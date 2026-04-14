#!/usr/bin/env bash
set -euo pipefail

uv sync
source .venv/bin/activate
python main.py
