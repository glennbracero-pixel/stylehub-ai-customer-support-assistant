from src.document_loader import load_documents


def test_load_documents_returns_five_documents():
    documents = load_documents()

    assert len(documents) == 5


def test_documents_have_filename_and_content():
    documents = load_documents()

    for document in documents:
        assert "filename" in document
        assert "content" in document
        assert document["filename"].endswith(".txt")
        assert document["content"].strip() != ""


def test_shipping_policy_is_loaded():
    documents = load_documents()

    filenames = [
        document["filename"]
        for document in documents
    ]

    assert "shipping_policy.txt" in filenames