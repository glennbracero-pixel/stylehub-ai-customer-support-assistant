
from sentence_transformers import SentenceTransformer

from src.process_documents import process_documents


MODEL_NAME = "all-MiniLM-L6-v2"


def generate_embeddings():
    """Convert document chunks into numerical embeddings."""

    print("Loading embedding model...")

    model = SentenceTransformer(MODEL_NAME)

    print("Loading document chunks...")

    chunks = process_documents()

    texts = [
        chunk["content"]
        for chunk in chunks
    ]

    print("Generating embeddings...")

    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    results = []

    for chunk, embedding in zip(chunks, embeddings):

        results.append({
            "filename": chunk["filename"],
            "chunk_number": chunk["chunk_number"],
            "content": chunk["content"],
            "embedding": embedding.tolist()
        })

    return results


if __name__ == "__main__":

    results = generate_embeddings()

    print(f"\nTotal embeddings generated: {len(results)}")

    if results:
        print(
            "Numbers in each embedding:",
            len(results[0]["embedding"])
        )

        print("\nFirst embedding preview:")
        print(results[0]["embedding"][:5])

    print("\nEmbedding generation completed successfully!")
