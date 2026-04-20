from typing import Any, Dict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from graph.state import GraphState

load_dotenv()


def _document_text(document: Any) -> str:
    if hasattr(document, "page_content"):
        return str(document.page_content)
    return str(document)


def _build_context(documents: list[Any]) -> str:
    return "\n\n".join(_document_text(doc) for doc in documents)


def generate(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]

    context = _build_context(documents)
    llm = ChatOpenAI(temperature=0)
    prompt = (
        "You are an assistant for question-answering tasks.\n"
        "Use the provided context to answer the question.\n"
        "If the answer cannot be found in the context, say you don't know.\n\n"
        f"Question: {question}\n\n"
        f"Context:\n{context}"
    )
    response = llm.invoke(prompt)
    generation = response.content if hasattr(response, "content") else str(response)

    return {"documents": documents, "question": question, "generation": generation}
