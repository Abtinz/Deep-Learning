from typing import Any, Dict

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_tavily import TavilySearch

from graph.state import GraphState

load_dotenv()
# Initialize the TavilySearch tool with a specified number of results to return
web_search_tool = TavilySearch(max_results=3)


def _extract_results(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        results = payload.get("results", [])
        return results if isinstance(results, list) else []
    return payload if isinstance(payload, list) else []


def _join_tavily_content(tavily_results: list[dict[str, Any]]) -> str:
    '''Joins the content from the TavilySearch results into a single string.
    Args:
        tavily_results: A list of dictionaries containing the results from the TavilySearch tool.   
    Returns:
        A single string containing the joined content from the TavilySearch results.
    '''
    return "\n".join(
        [result["content"] for result in tavily_results if "content" in result]
    )


def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")

    # Extract the question and any existing documents from the graph state
    question = state["question"]
    documents = state.get("documents")
    
    # Use the TavilySearch tool to perform a web search based on the question
    raw_results = web_search_tool.invoke({"query": question})
    tavily_results = _extract_results(raw_results)

    joined_tavily_result = _join_tavily_content(tavily_results)
    print(f"---WEB SEARCH--- Retrieved {len(tavily_results)} web results.")

    # Create a Document object to store the joined TavilySearch results
    web_results = Document(
        page_content=joined_tavily_result
    )

    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]

    return {"documents": documents, "question": question}
