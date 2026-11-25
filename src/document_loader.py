
from pathlib import Path


# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Find the documents folder
DOCUMENTS_FOLDER = PROJECT_ROOT / "documents"


def load_documents():
    """Load all text documents from the knowledge base."""

    documents = []

    # Find all .txt files
    for file_path in DOCUMENTS_FOLDER.glob("*.txt"):

        # Read the document contents
        content = file_path.read_text(
            encoding="utf-8"
        )

        # Store the filename and its content
        documents.append({
            "filename": file_path.name,
            "content": content
        })

    return documents


if __name__ == "__main__":

    loaded_documents = load_documents()

    print(f"Documents loaded: {len(loaded_documents)}")

    for document in loaded_documents:
        print(f"\nFile: {document['filename']}")
        print(f"Characters: {len(document['content'])}")

    print("\nAll documents loaded successfully!")
