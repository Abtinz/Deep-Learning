import importlib
from types import SimpleNamespace

grade_documents_module = importlib.import_module("graph.nodes.grade_documents")
from graph.nodes.grade_documents import grade_documents


def test_grade_documents_filters_irrelevant_docs_and_triggers_web_search(monkeypatch) -> None:
    class DummyGrader:
        def invoke(self, payload):
            text = payload["document"]
            score = "no" if "irrelevant" in text else "yes"
            return SimpleNamespace(binary_score=score)

    monkeypatch.setattr(grade_documents_module, "retrieval_grader", DummyGrader())

    state = {
        "question": "What is agent memory?",
        "documents": [
            SimpleNamespace(page_content="Agent memory stores prior context."),
            SimpleNamespace(page_content="irrelevant pizza recipe"),
        ],
    }

    result = grade_documents(state)

    assert len(result["documents"]) == 1
    assert result["documents"][0].page_content == "Agent memory stores prior context."
    assert result["web_search"] is True


def test_grade_documents_supports_plain_string_documents(monkeypatch) -> None:
    class DummyGrader:
        def invoke(self, payload):
            return SimpleNamespace(binary_score="yes")

    monkeypatch.setattr(grade_documents_module, "retrieval_grader", DummyGrader())

    state = {
        "question": "What is retrieval?",
        "documents": ["Retriever fetches semantically similar chunks."],
    }

    result = grade_documents(state)

    assert result["documents"] == ["Retriever fetches semantically similar chunks."]
    assert result["web_search"] is False
