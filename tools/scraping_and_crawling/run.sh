#!/usr/bin/env sh
set -eu

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

sh ./setup_env.sh
. ./.venv/bin/activate
python ./crawl_demo.py
