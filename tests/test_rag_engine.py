from unittest.mock import Mock

from src.rag_engine import get_relevant_context


def create_mock_model():
    """Create a simulated embedding model."""
    embedding = Mock()
    embedding.tolist.return_value = [0.1, 0.2, 0.3]

    model = Mock()
    model.encode.return_value = embedding

    return model


def test_relevant_information_is_retrieved():
    collection = Mock()

    collection.query.return_value = {
        "documents": [[
            "Standard shipping costs $5.99.",
            "Express shipping costs $12.99."
        ]],
        "distances": [[0.20, 0.30]]
    }

    model = create_mock_model()

    context = get_relevant_context(
        "How much does shipping cost?",
        collection,
        model
    )

    assert "Standard shipping costs $5.99." in context
    assert "Express shipping costs $12.99." in context


def test_irrelevant_information_is_rejected():
    collection = Mock()

    collection.query.return_value = {
        "documents": [[
            "StyleHub offers a student discount."
        ]],
        "distances": [[0.90]]
    }

    model = create_mock_model()

    context = get_relevant_context(
        "Do you offer student discounts?",
        collection,
        model
    )

    assert context == ""

from unittest.mock import patch

from src.rag_engine import generate_answer


def test_answer_is_generated_from_relevant_context():
    collection = Mock()
    model = create_mock_model()

    with patch(
        "src.rag_engine.get_relevant_context",
        return_value="Standard shipping costs $5.99."
    ), patch(
        "src.rag_engine.ask_ollama",
        return_value="Standard shipping costs $5.99."
    ) as mock_ai:

        answer = generate_answer(
            "How much does shipping cost?",
            collection,
            model
        )

    assert "Standard shipping costs $5.99." in answer
    mock_ai.assert_called_once()


def test_missing_information_returns_fallback():
    collection = Mock()
    model = create_mock_model()

    with patch(
        "src.rag_engine.get_relevant_context",
        return_value=""
    ), patch(
        "src.rag_engine.ask_ollama"
    ) as mock_ai:

        answer = generate_answer(
            "Do you offer student discounts?",
            collection,
            model
        )

    assert "I don't have enough information" in answer
    mock_ai.assert_not_called()


def test_ai_connection_failure_returns_none():
    collection = Mock()
    model = create_mock_model()

    with patch(
        "src.rag_engine.get_relevant_context",
        return_value="Standard shipping costs $5.99."
    ), patch(
        "src.rag_engine.ask_ollama",
        return_value=None
    ):

        answer = generate_answer(
            "How much does shipping cost?",
            collection,
            model
        )

    assert answer is None