import os
from pathlib import Path

from dotenv import load_dotenv
from dotenv import dotenv_values
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter


load_dotenv()


def load_env_params(env_path: str | Path = ".env") -> dict[str, str]:
    raw_params = dotenv_values(env_path)
    return {k: v for k, v in raw_params.items() if v is not None}


def run_ingestion(
    source_path: str | Path = "mediumblog1.txt",
    chunk_size: int = 1000,
    chunk_overlap: int = 0,
    dry_run: bool = False,
) -> dict[str, int | str | bool]:
    source_path = Path(source_path)

    print("SECTION 1: Load source document")
    loader = TextLoader(str(source_path))
    documents = loader.load()
    print(f"Loaded {len(documents)} document(s) from {source_path}")

    print("\nSECTION 2: Split document into chunks")
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunk(s)")
    if chunks:
        preview = chunks[0].page_content[:180].replace("\n", " ")
        print(f"First chunk preview: {preview}...")

    if dry_run:
        print("\nSECTION 3: Dry run mode enabled - skipping embedding + Pinecone ingest")
        return {
            "source_path": str(source_path),
            "document_count": len(documents),
            "chunk_count": len(chunks),
            "ingested": False,
        }

    print("\nSECTION 3: Create embeddings")
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    print("Embeddings client initialized")

    print("\nSECTION 4: Ingest into Pinecone index")
    index_name = os.environ["INDEX_NAME"]
    PineconeVectorStore.from_documents(chunks, embeddings, index_name=index_name)
    print(f"Ingested {len(chunks)} chunk(s) into index '{index_name}'")

    return {
        "source_path": str(source_path),
        "document_count": len(documents),
        "chunk_count": len(chunks),
        "ingested": True,
    }


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parent
    run_ingestion(source_path=project_dir / "mediumblog1.txt")
