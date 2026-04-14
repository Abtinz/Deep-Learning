from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from react import llm, tools

load_dotenv()

SYSYEM_MESSAGE = """
You are a tool-using research assistant.

When using web search and crawl tools:
1. Prefer official, trusted sources first.
2. Validate crawl output quality before finalizing:
   - Is the content relevant to the user question?
   - Does it contain concrete facts (not empty/noisy text)?
   - Is the source credible for the topic?
3. If crawl output is invalid, empty, or low quality, search again and pick a better source.
4. Retry search/crawl at most 2 times, then provide the best available answer and clearly state limits.
5. Do not repeat the same failing crawl input over and over.

After tools complete, return a concise final answer.
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run the agent reasoning node.
    This node takes the current conversation state, invokes the LLM with the system prompt and conversation history,
    and returns the updated conversation state with the LLM's response.
    Args:
        state: The current conversation state, including the message history.
    Returns:
        An updated conversation state with the LLM's response added to the message history.
    """
    response = llm.invoke([{"role": "system", "content": SYSYEM_MESSAGE}, *state["messages"]])
    return {"messages": [response]}

tool_node = ToolNode(tools)
