from dotenv import load_dotenv
from langgraph.graph import END, StateGraph

from graph.consts import GENERATE, GRADE_DOCUMENTS, RETRIEVE, WEBSEARCH
from graph.nodes import generate, grade_documents, retrieve, web_search
from graph.state import GraphState

load_dotenv()

def decide_to_generate(state: GraphState) -> str:
    '''Decides whether to proceed with generating an answer or to perform a web search based on the relevance of retrieved documents.
    Args:
        state: The current state of the graph, containing the question, retrieved documents, and a flag indicating whether web search is needed.
    Returns:
        A string indicating the next node to execute, either 'WEBSEARCH' or 'GENERATE'.
    '''

    print("---ASSESS GRADED DOCUMENTS---")

    if state["web_search"]:
        print("---DECISION: INCLUDE WEB SEARCH---")
        return WEBSEARCH

    print("---DECISION: GENERATE---")
    return GENERATE


workflow = StateGraph(GraphState)
# Add nodes to the graph and define the edges between them
workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)

# Define the edges between the nodes
# including conditional edges based on the output of the GRADE_DOCUMENTS node
workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate,
    {WEBSEARCH: WEBSEARCH, GENERATE: GENERATE},
)
workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()
