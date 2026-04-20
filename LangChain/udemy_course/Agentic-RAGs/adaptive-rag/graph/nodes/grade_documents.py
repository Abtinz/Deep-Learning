from typing import Any, Dict

from graph.chains.retrieval_grader import retrieval_grader
from graph.state import GraphState


def _document_text(document: Any) -> str:
    if hasattr(document, "page_content"):
        return str(document.page_content)
    return str(document)


def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
    Determines whether retrieved documents are relevant to the question.
    If any document is not relevant, set a flag to run web search.
    """

    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    question = state["question"]
    documents = state["documents"]

    filtered_docs = []
    web_search = False

    for document in documents:
        score = retrieval_grader.invoke(
            {"question": question, "document": _document_text(document)}
        )
        grade = score.binary_score.lower()

        if grade == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_docs.append(document)
        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            web_search = True

    if not filtered_docs:
        web_search = True

    return {"documents": filtered_docs, "question": question, "web_search": web_search}
