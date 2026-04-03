# SymanticSearch

This folder contains semantic-search projects using embeddings and vector retrieval.

## What Semantic Search Means Here

- Semantic search retrieves by meaning, not exact keyword matching.
- Text is transformed into embeddings, then queried by vector similarity.
- Retrieval quality depends on embedding model choice, chunking, and vector index configuration.

## Core Concepts Implemented

- Embedding generation for documents and queries.
- Vector index creation and management.
- Batch upsert and namespace usage.
- Similarity query and result inspection.
- Vector cleanup/delete workflows.

## Projects In This Folder

- `Simantic_Search_OpenAI(ada3)_and_Pinecone.ipynb`
  - OpenAI embeddings + Pinecone retrieval pipeline.
- `Text_Embedding_with_Pretrained_model.ipynb`
  - Embedding and retrieval workflow with pretrained models + Pinecone.

## Models and Technologies Referenced

- OpenAI embedding families (Ada references in project naming/content).
- Pinecone vector database (`Pinecone`, `ServerlessSpec`).

