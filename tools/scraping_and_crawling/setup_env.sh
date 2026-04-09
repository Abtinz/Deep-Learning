#!/usr/bin/env sh
set -eu

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

. .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt ipykernel

KERNEL_NAME="scraping-and-crawling"
python -m ipykernel install --user --name "$KERNEL_NAME" --display-name "Python (scraping-and-crawling)"

echo
echo "Environment ready."
echo "Kernel installed: Python (scraping-and-crawling)"
echo "To activate manually later:"
echo "source \"$SCRIPT_DIR/.venv/bin/activate\""
