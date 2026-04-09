# Documentation Helper

Documentation Helper is a small LangChain workflow for building a local documentation question-answering assistant. It is designed to ingest LangChain documentation into a vector store and then use retrieval-augmented generation to answer user questions with grounded context.

The ingestion notebook prepares the data layer by crawling documentation pages, converting them into documents, splitting them into chunks, generating embeddings, and storing them in a local Chroma database. This step creates the searchable knowledge base used by the rest of the project.

The core notebook focuses on runtime question answering. It initializes the chat model and retrieval tool, fetches the most relevant chunks from Chroma, and produces answers based on retrieved context instead of relying only on model memory. This makes responses more relevant to the indexed docs and easier to trace back to sources.

This project is useful when you want a practical end-to-end template for documentation RAG in notebooks, especially for Colab-style workflows where setup, ingestion, and querying are run interactively in sequence.
