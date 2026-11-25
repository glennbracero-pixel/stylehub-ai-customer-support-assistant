
import re


def split_text(text, chunk_size=500, overlap=100):
    """Split text at natural boundaries while preserving overlap."""

    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "Overlap must be non-negative and smaller than chunk size."
        )

    chunks = []
    start = 0

    while start < len(text):
        max_end = min(start + chunk_size, len(text))

        if max_end == len(text):
            end = max_end
        else:
            window = text[start:max_end]
            minimum_split = len(window) // 2

            # Prefer paragraph boundaries.
            paragraph_end = window.rfind("\n\n", minimum_split)

            # Otherwise, prefer sentence boundaries.
            sentence_matches = list(
                re.finditer(
                    r'[.!?]["\')\]]?\s+',
                    window[minimum_split:]
                )
            )

            if paragraph_end != -1:
                end = start + paragraph_end + 2

            elif sentence_matches:
                end = (
                    start
                    + minimum_split
                    + sentence_matches[-1].end()
                )

            else:
                # Fall back to a word boundary.
                word_end = window.rfind(" ", minimum_split)

                if word_end != -1:
                    end = start + word_end
                else:
                    # No natural boundary: split at the size limit.
                    end = max_end

        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        if end >= len(text):
            break

        start = max(end - overlap, start + 1)

    return chunks


if __name__ == "__main__":
    sample_text = """
StyleHub offers standard shipping and express shipping.

Standard shipping costs $5.99, while express shipping
costs $12.99. Orders of $75 or more qualify for free
standard shipping.

Delivery times may vary depending on the destination.
"""

    results = split_text(
        sample_text,
        chunk_size=100,
        overlap=20
    )

    print(f"Total chunks: {len(results)}")

    for number, chunk in enumerate(results, start=1):
        print(f"\nChunk {number}:")
        print(chunk)

    print("\nText splitting completed successfully!")
