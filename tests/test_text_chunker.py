import pytest

from src.text_chunker import split_text


def test_text_is_split_into_multiple_chunks():
    text = "A" * 1200

    chunks = split_text(
        text,
        chunk_size=500,
        overlap=100
    )

    assert len(chunks) == 3


def test_chunks_have_overlapping_content():
    text = "A" * 900

    chunks = split_text(
        text,
        chunk_size=500,
        overlap=100
    )

    assert chunks[0][-100:] == chunks[1][:100]


def test_invalid_chunk_size_raises_error():
    with pytest.raises(ValueError):
        split_text("Sample text", chunk_size=0)


def test_invalid_overlap_raises_error():
    with pytest.raises(ValueError):
        split_text("Sample text", chunk_size=100, overlap=100)