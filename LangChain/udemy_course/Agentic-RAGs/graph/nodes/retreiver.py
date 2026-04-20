from typing import Any, Dict

from graph.state import GraphState
from ingestion.retreiver import retriever

def retrieve(state: GraphState) -> Dict[str, Any]:
    '''Retrieves relevant documents based on the question in the graph state.
    
    Args:
        state: The current state of the graph, containing the question and other relevant information.
    Returns:
        A dictionary containing the retrieved documents and the original question.
    '''
    print("---RETRIEVE---")
    print(f"---RETRIEVE--- Question: {state['question']}")

    question = state["question"]

    documents = retriever.invoke(question)

    results = [doc.page_content for doc in documents]
    
    print(f"---RETRIEVE--- Retrieved {len(results)} documents.")
    
    return {"documents": documents, "question": question}
