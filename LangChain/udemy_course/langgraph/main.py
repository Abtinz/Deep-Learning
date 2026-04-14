from dotenv import load_dotenv

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph,END

from nodes import run_agent_reasoning, tool_node

load_dotenv()

# Define constants for node names and flow control
AGENT_REASON="agent_reason"
ACT= "act"
LAST = -1
MAX_MESSAGES = 14

def should_continue(state: MessagesState) -> str:
    """
    Determine whether to continue the agent reasoning loop or end it.
    This function checks the current conversation state to see if the maximum number of messages has been reached
    or if there are no tool calls in the last message. If either condition is met, it returns 'END' to stop the loop;
    otherwise, it returns 'ACT' to continue with another iteration of reasoning and tool use.
    Args:
        state: The current conversation state, including the message history.  
    Returns:
        A string indicating whether to continue ('ACT') or end ('END') the agent reasoning loop.
    """
    if len(state["messages"]) >= MAX_MESSAGES:
        return END
    if not state["messages"][LAST].tool_calls:
        return END
    return ACT

flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_node)

flow.add_conditional_edges(
    AGENT_REASON, 
    should_continue, 
    { END:END, ACT:ACT }
)

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()
app.get_graph().draw_mermaid_png(output_file_path="flow.png")

if __name__ == "__main__":

    print("Hello ReAct LangGraph with Function Calling")
    
    res = app.invoke(
        {
            "messages": [
                HumanMessage(
                    content="What is the temperature in Tokyo? search for <accuweather> website, crawl it data about japan, savethe results, and List it and then triple it"
                )
            ]
        },
        config={"recursion_limit": 12},
    )

print(res["messages"][LAST].content)
