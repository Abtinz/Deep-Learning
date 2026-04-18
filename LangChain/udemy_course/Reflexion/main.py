from typing import Literal, Sequence

from langchain_core.messages import AIMessage, BaseMessage, ToolMessage
from langgraph.graph import END, START, MessagesState, StateGraph

from chains import first_responder, revisor
from tool_executor import execute_tools

MAX_ITERATIONS = 2


def draft_node(state: MessagesState):
    """Draft the initial response."""
    response = first_responder.invoke({"messages": state["messages"]})
    return {"messages": [response]}


def revise_node(state: MessagesState):
    """Revise the answer based on tool results."""
    response = revisor.invoke({"messages": state["messages"]})
    return {"messages": [response]}


def event_loop(state: MessagesState) -> Literal["execute_tools", END]:
    """Determine whether to continue or end based on iteration count."""
    tool_visits = sum(isinstance(item, ToolMessage) for item in state["messages"])
    if tool_visits > MAX_ITERATIONS:
        return END
    return "execute_tools"


def build_graph():
    """Build and compile the Reflexion workflow graph."""
    builder = StateGraph(MessagesState)
    builder.add_node("draft", draft_node)
    builder.add_node("execute_tools", execute_tools)
    builder.add_node("revise", revise_node)
    builder.add_edge(START, "draft")
    builder.add_edge("draft", "execute_tools")
    builder.add_edge("execute_tools", "revise")
    builder.add_conditional_edges("revise", event_loop, ["execute_tools", END])
    return builder.compile()


graph = build_graph()


def extract_final_answer(messages: Sequence[BaseMessage]) -> str:
    """Extract the last tool-call answer payload from graph messages."""
    for message in reversed(messages):
        if not isinstance(message, AIMessage) or not message.tool_calls:
            continue
        for tool_call in message.tool_calls:
            args = tool_call.get("args", {})
            if isinstance(args, dict) and "answer" in args:
                return args["answer"]
    raise ValueError("No final answer found in agent output.")


def run_reflexion(question: str) -> str:
    """Run the Reflexion graph on a user question and return the final answer text."""
    result = graph.invoke({"messages": [{"role": "user", "content": question}]})
    return extract_final_answer(result["messages"])


if __name__ == "__main__":
    graph.get_graph().draw_mermaid_png(output_file_path="reflexion_agent.png")
    demo_question = (
        "Write about AI-Powered SOC / autonomous soc problem domain, "
        "list startups that do that and raised capital."
    )
    print(run_reflexion(demo_question))
