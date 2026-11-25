from pathlib import Path

import chromadb

from src.embedding_generator import generate_embeddings


# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Set the database location
DB_PATH = PROJECT_ROOT / "data" / "chroma_db"

# Name our knowledge collection
COLLECTION_NAME = "stylehub_knowledge"


def create_vector_store():
    """Save document chunks and embeddings in ChromaDB."""

    print("Generating document embeddings...")

    records = generate_embeddings()

    print("Connecting to ChromaDB...")

    client = chromadb.PersistentClient(
        path=str(DB_PATH)
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )

    print("Saving embeddings to the database...")

    collection.upsert(
        ids=[
            f"{record['filename']}__{record['chunk_number']}"
            for record in records
        ],
        embeddings=[
            record["embedding"]
            for record in records
        ],
        documents=[
            record["content"]
            for record in records
        ],
        metadatas=[
            {
                "filename": record["filename"],
                "chunk_number": record["chunk_number"]
            }
            for record in records
        ]
    )

    print(f"\nRecords saved: {collection.count()}")

    print(f"Database location: {DB_PATH}")

    return collection


if __name__ == "__main__":

    collection = create_vector_store()

    print("\nTesting database retrieval...")

    results = collection.query(
        query_texts=["How much does standard shipping cost?"],
        n_results=3
    )

    for document in results["documents"][0]:

        print("\nRetrieved information:")
        print(document)

    print("\nDatabase retrieval test completed!")