from typing import TypedDict, Annotated

from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

from chains import generate_chain, reflect_chain

REFLECT = "reflect"
GENERATE = "generate"

class MessageGraph(TypedDict):
    '''The MessageGraph state schema, which defines the structure of the conversation state used in the LangGraph application.
    This schema includes a list of messages, where each message is an instance of BaseMessage (or its subclasses like HumanMessage).
    The add_messages function is used as an annotation to specify how messages
    should be added to the state when new messages are generated during the graph execution.
    '''
    messages: Annotated[list[BaseMessage], add_messages]

def generation_node(state: MessageGraph):
    '''The generation node function, which takes the current conversation state (MessageGraph) as input and returns an updated state with the LLM's generated tweet.
    This function invokes the generate_chain with the current messages in the state, which generates a new
        tweet based on the user's request and any previous messages. The response from the generate_chain is then returned as the new state for the next iteration of the graph.
        Args:
            state: The current conversation state, including the message history.
        Returns:
            An updated conversation state with the LLM's generated tweet added as a HumanMessage.
    '''
    return {"messages": [generate_chain.invoke({"messages": state["messages"]})]}


def reflection_node(state: MessageGraph):
    '''The reflection node function, which takes the current conversation state (MessageGraph) as input and returns an updated state with the LLM's critique and recommendations.
    This function invokes the reflect_chain with the current messages in the state, which generates a critique
    and recommendations for improving the user's tweet. The response from the reflect_chain is then wrapped in a HumanMessage and returned as the new state for the next iteration of the graph.
    Args:
        state: The current conversation state, including the message history.
    Returns:
        An updated conversation state with the LLM's critique and recommendations added as a HumanMessage.
    '''
    res = reflect_chain.invoke({"messages": state["messages"]})
    return {"messages": [HumanMessage(content=res.content)]}

def should_continue(state: MessageGraph):
    '''Determine whether to continue the agent reasoning loop or end it.
    This function checks the current conversation state to see if the maximum number of messages has been reached
    or if there are no tool calls in the last message. If either condition is met,
    it returns 'END' to stop the loop; otherwise, it returns 'REFLECT' to continue with another iteration of reasoning and reflection.
    Args:
        state: The current conversation state, including the message history.
    Returns:
        A string indicating whether to continue ('REFLECT') or end ('END') the agent reasoning loop.
    '''
    if len(state["messages"]) > 6:
        return END
    return REFLECT

builder = StateGraph(state_schema=MessageGraph)
builder.add_node(GENERATE, generation_node)
builder.add_node(REFLECT, reflection_node)
builder.set_entry_point(GENERATE)

builder.add_conditional_edges(GENERATE, should_continue)
builder.add_edge(REFLECT, GENERATE)

graph = builder.compile()

graph.get_graph().draw_mermaid_png(output_file_path="reflection_agent.png")

if __name__ == "__main__":
    print("Hello LangGraph")
    inputs = {
        "messages": [
            HumanMessage(
                content="""Make this tweet better:"
                                    @LangChainAI
            — newly Tool Calling feature is seriously underrated.

            After a long wait, it's  here- making the implementation of agents across different models with function calling - super easy.

            Made a video covering their newest blog post

            """
            )
        ]
    }
    response = graph.invoke(inputs)
    
    print(response)
