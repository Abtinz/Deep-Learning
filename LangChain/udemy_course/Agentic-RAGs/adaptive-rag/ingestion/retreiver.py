from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from ingestion.configs import COLLECTION_NAME, PERSIST_DIRECTORY

embedding_function=OpenAIEmbeddings()

retriever = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory=PERSIST_DIRECTORY,
    embedding_function=embedding_function,
).as_retriever()