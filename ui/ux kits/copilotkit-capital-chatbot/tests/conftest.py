"""Pytest configuration for project import paths."""

import sys
from pathlib import Path


# Add the project root to sys.path so test modules can import app code.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
