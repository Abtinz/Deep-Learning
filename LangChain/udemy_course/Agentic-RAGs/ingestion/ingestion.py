from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from ingestion.configs import CHUNK_OVERLAP, CHUNK_SIZE, URLS, COLLECTION_NAME, PERSIST_DIRECTORY

load_dotenv()

embedding_function=OpenAIEmbeddings()

docs = [WebBaseLoader(url).load() for url in URLS]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=CHUNK_SIZE, 
    chunk_overlap=CHUNK_OVERLAP
)

doc_splits = text_splitter.split_documents(docs_list)

vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name=COLLECTION_NAME,
    embedding=embedding_function,
    persist_directory=PERSIST_DIRECTORY,
)