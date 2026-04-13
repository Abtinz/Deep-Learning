from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from LangChain.udemy_course.RAGs.Medium_analyzer.ingestion import load_env_params, run_ingestion


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


def test_run_ingestion_dry_run_returns_pipeline_summary():
    source_path = PROJECT_ROOT / "mediumblog1.txt"
    summary = run_ingestion(source_path=source_path, dry_run=True)

    assert summary["source_path"] == str(source_path)
    assert summary["document_count"] > 0
    assert summary["chunk_count"] > 0
    assert summary["ingested"] is False
