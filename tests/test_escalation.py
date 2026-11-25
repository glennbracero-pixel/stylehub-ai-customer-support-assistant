from src.escalation import requires_human_support


def test_shipping_question_does_not_require_human():
    assert requires_human_support(
        "How much does shipping cost?"
    ) is False


def test_damaged_order_requires_human():
    assert requires_human_support(
        "My order arrived damaged."
    ) is True


def test_duplicate_charge_requires_human():
    assert requires_human_support(
        "I was charged twice."
    ) is True


def test_human_support_request_requires_human():
    assert requires_human_support(
        "I want to speak to a human."
    ) is True