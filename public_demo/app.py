
import streamlit as st


st.set_page_config(
    page_title="StyleHub Support Demo",
    page_icon="👕",
    layout="centered"
)


# Sample business knowledge for the public demo.
DEMO_KNOWLEDGE = {
    "shipping": (
        "StyleHub offers standard shipping for $5.99. "
        "Orders over $75 qualify for free standard shipping. "
        "Standard delivery usually takes 3–5 business days."
    ),
    "returns": (
        "StyleHub accepts returns within 30 days of delivery. "
        "Items must be unused and in their original condition. "
        "Refunds are processed to the original payment method "
        "after the returned item is inspected."
    ),
    "payment": (
        "StyleHub accepts major credit cards and debit cards. "
        "Payment is collected securely during checkout."
    ),
    "products": (
        "StyleHub offers everyday clothing, including "
        "shirts, jeans, jackets, and casual accessories. "
        "Product availability may vary."
    ),
    "tracking": (
        "After your order ships, you will receive a confirmation "
        "email containing tracking information. "
        "Please contact customer support if you need help "
        "with a specific order."
    )
}


def get_demo_answer(question):
    """Return a sample response based on the customer's question."""

    question = question.lower()

    if any(word in question for word in ["refund", "return"]):
        return DEMO_KNOWLEDGE["returns"]

    if any(word in question for word in ["shipping", "delivery", "cost"]):
        return DEMO_KNOWLEDGE["shipping"]

    if any(word in question for word in ["payment", "pay", "card"]):
        return DEMO_KNOWLEDGE["payment"]

    if any(word in question for word in ["product", "clothes", "shirt", "jeans"]):
        return DEMO_KNOWLEDGE["products"]

    if any(word in question for word in ["track", "tracking", "order"]):
        return DEMO_KNOWLEDGE["tracking"]

    return (
        "I don't have enough information to answer that question "
        "in this demonstration. Please contact StyleHub Customer "
        "Support for further assistance."
    )


def requires_human_support(question):
    """Identify requests that should be reviewed by a human."""

    keywords = [
        "complaint",
        "damaged",
        "wrong order",
        "missing order",
        "chargeback",
        "cancel my order",
        "speak to a person",
        "human support"
    ]

    question = question.lower()

    return any(keyword in question for keyword in keywords)


st.title("👕 StyleHub Customer Support")

st.caption("Interactive Public Portfolio Demonstration")

st.info(
    "Demo mode: This version uses sample business information "
    "and predefined responses. It does not connect to a live "
    "store, customer accounts, or the original local AI system."
)


st.write(
    "Welcome to StyleHub! Ask a question about shipping, "
    "returns, refunds, payments, or products."
)


suggested_questions = [
    "How much does shipping cost?",
    "What is your return policy?",
    "What payment methods do you accept?",
    "How can I track my order?"
]


if "messages" not in st.session_state:
    st.session_state.messages = []


st.write("**Popular questions:**")

columns = st.columns(2)

for index, suggested_question in enumerate(suggested_questions):
    with columns[index % 2]:
        if st.button(suggested_question, use_container_width=True):
            st.session_state.selected_question = suggested_question


st.divider()


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("escalation"):
            st.warning(
                "Human Support Recommended: "
                "This request may need personal assistance."
            )


question = st.chat_input("How can we help you today?")

if not question:
    question = st.session_state.pop("selected_question", None)


if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    answer = get_demo_answer(question)
    escalation = requires_human_support(question)

    with st.chat_message("assistant"):
        st.markdown(answer)

        if escalation:
            st.warning(
                "Human Support Recommended: "
                "Please contact the StyleHub support team "
                "for personal assistance."
            )

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "escalation": escalation
    })


with st.sidebar:
    st.subheader("About StyleHub")

    st.write(
        "Your online clothing store for comfortable "
        "and everyday fashion."
    )

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.caption(
        "This is a sample portfolio demonstration. "
        "All business information and responses are illustrative."
    )
