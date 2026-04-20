from graph.consts import GENERATE, WEBSEARCH
from graph.graph import decide_to_generate


def test_decide_to_generate_routes_to_websearch_when_flagged() -> None:
    state = {"web_search": True}
    assert decide_to_generate(state) == WEBSEARCH


def test_decide_to_generate_routes_to_generate_when_not_flagged() -> None:
    state = {"web_search": False}
    assert decide_to_generate(state) == GENERATE
