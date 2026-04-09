from typing import Any, Dict

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import ToolMessage
from langchain.tools import tool
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# Initialize embeddings (same as ingestion.py)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Initialize local Chroma vector store.
# Make sure ingestion ran first and populated this directory.
vectorstore = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

# Initialize chat model
model = init_chat_model("gpt-5.2", model_provider="openai")


@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve relevant documentation to help answer user queries about LangChain."""
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    retrieved_docs = retriever.invoke(query)

    serialized = "\n\n".join(
        (
            f"Source: {doc.metadata.get('source', 'Unknown')}\n\n"
            f"Content: {doc.page_content}"
        )
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


def run_llm(query: str) -> Dict[str, Any]:
    """
    Run the RAG pipeline to answer a query using retrieved documentation.

    Args:
        query: The user's question.

    Returns:
        Dictionary containing:
            - answer: The generated answer.
            - context: List of retrieved documents.
    """
    system_prompt = (
        "You are a helpful AI assistant that answers questions about LangChain documentation. "
        "You have access to a tool that retrieves relevant documentation. "
        "Use the tool to find relevant information before answering questions. "
        "Always cite the sources you use in your answers. "
        "If you cannot find the answer in the retrieved documentation, say so."
    )

    agent = create_agent(model, tools=[retrieve_context], system_prompt=system_prompt)
    response = agent.invoke({"messages": [{"role": "user", "content": query}]})
    answer = response["messages"][-1].content

    context_docs = []
    for message in response["messages"]:
        if isinstance(message, ToolMessage) and hasattr(message, "artifact"):
            if isinstance(message.artifact, list):
                context_docs.extend(message.artifact)

    return {"answer": answer, "context": context_docs}


if __name__ == "__main__":
    result = run_llm(query="what are deep agents?")
    print(result)
