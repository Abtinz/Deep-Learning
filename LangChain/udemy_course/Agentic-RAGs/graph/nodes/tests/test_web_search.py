from types import SimpleNamespace

from graph.nodes.web_search import web_search


def test_web_search_appends_tavily_results_to_existing_documents(monkeypatch) -> None:
    class DummySearch:
        def invoke(self, payload):
            assert payload["query"] == "agent memory"
            return [
                {"content": "First result"},
                {"content": "Second result"},
            ]

    monkeypatch.setattr("graph.nodes.web_search.web_search_tool", DummySearch())

    existing = [SimpleNamespace(page_content="Existing doc")]
    result = web_search({"question": "agent memory", "documents": existing})

    assert len(result["documents"]) == 2
    assert result["documents"][1].page_content == "First result\nSecond result"


def test_web_search_creates_documents_list_when_none(monkeypatch) -> None:
    class DummySearch:
        def invoke(self, payload):
            return [{"content": "Only result"}]

    monkeypatch.setattr("graph.nodes.web_search.web_search_tool", DummySearch())

    result = web_search({"question": "agent memory", "documents": None})

    assert len(result["documents"]) == 1
    assert result["documents"][0].page_content == "Only result"
