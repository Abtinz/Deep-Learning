from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ingestion import load_env_params


def test_load_env_params_returns_required_keys():
    env_path = PROJECT_ROOT / ".env"
    params = load_env_params(env_path)

    required_keys = {
        "OPENAI_API_KEY",
        "LANGSMITH_API_KEY",
        "LANGSMITH_PROJECT",
        "LANGSMITH_TRACING",
        "INDEX_NAME",
        "PINECONE_API_KEY",
    }

    assert required_keys.issubset(params.keys())