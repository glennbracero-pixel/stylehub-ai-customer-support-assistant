
from src.document_loader import load_documents
from src.text_chunker import split_text


def process_documents():
    """Load company documents and split them into chunks."""

    documents = load_documents()

    all_chunks = []

    for document in documents:

        chunks = split_text(
            document["content"],
            chunk_size=500,
            overlap=100
        )

        for chunk_number, chunk in enumerate(chunks, start=1):

            all_chunks.append({
                "filename": document["filename"],
                "chunk_number": chunk_number,
                "content": chunk
            })

    return all_chunks


if __name__ == "__main__":

    chunks = process_documents()

    print(f"Documents processed: 5")
    print(f"Total chunks created: {len(chunks)}")

    for chunk in chunks:
        print(
            f"\nFile: {chunk['filename']} "
            f"| Chunk: {chunk['chunk_number']}"
        )

        print(chunk["content"][:100] + "...")

    print("\nAll documents processed successfully!")
