
ESCALATION_KEYWORDS = [
    "damaged",
    "broken",
    "defective",
    "incorrect item",
    "wrong item",
    "duplicate charge",
    "charged twice",
    "payment dispute",
    "dispute my payment",
    "refund exception",
    "return exception",
    "speak to a human",
    "talk to a person",
    "human support",
    "customer service representative"
]


def requires_human_support(question):
    """Check whether a customer question needs human attention."""

    normalized_question = question.lower()

    for keyword in ESCALATION_KEYWORDS:
        if keyword in normalized_question:
            return True

    return False


if __name__ == "__main__":
    test_questions = [
        "How much does shipping cost?",
        "My order arrived damaged.",
        "I was charged twice.",
        "Do you offer student discounts?",
        "I want to speak to a human."
    ]

    for question in test_questions:
        result = requires_human_support(question)

        print(f"\nQuestion: {question}")
        print(f"Human support required: {result}")
