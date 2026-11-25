
import streamlit as st
import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer

from src.rag_engine import generate_answer
from src.escalation import requires_human_support


st.set_page_config(
    page_title="StyleHub Customer Support",
    page_icon="👕",
    layout="centered"
)


@st.cache_resource
def load_embedding_model():
    """Load and cache the embedding model."""
    return SentenceTransformer("all-MiniLM-L6-v2")


@st.cache_resource
def load_knowledge_base():
    """Connect to the existing ChromaDB knowledge base."""
    project_root = Path(__file__).resolve().parent

    client = chromadb.PersistentClient(
        path=str(project_root / "data" / "chroma_db")
    )

    return client.get_collection(
        name="stylehub_knowledge"
    )


st.title("👕 StyleHub Customer Support")


st.write(
    "Welcome to StyleHub! Ask me about shipping, "
    "returns, refunds, payments, or our products."
)

st.write("**Popular questions:**")

suggested_questions = [
    "How much does shipping cost?",
    "What is your return policy?",
    "What payment methods do you accept?",
    "How can I track my order?"
]

columns = st.columns(2)

for index, suggested_question in enumerate(suggested_questions):
    with columns[index % 2]:
        if st.button(
            suggested_question,
            use_container_width=True
        ):
            st.session_state["selected_question"] = suggested_question

st.divider()



# Load the AI model and company knowledge base.
with st.spinner("Preparing the customer support assistant..."):
    embedding_model = load_embedding_model()
    collection = load_knowledge_base()


# Initialize conversation history.
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("escalation"):
            st.warning(
                "Human Support Recommended: "
                "This request may need personal assistance "
                "from the StyleHub Customer Support team."
            )


# Receive a new customer question.
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

    # Generate the AI response.
    with st.chat_message("assistant"):
        with st.spinner("Looking for the right information..."):

            answer = generate_answer(
                question,
                collection,
                embedding_model
            )

            if answer is None:
                answer = (
                    "I'm sorry, but I'm having trouble "
                    "connecting to our support assistant. "
                    "Please try again later."
                )

            escalation = requires_human_support(question)

            st.markdown(answer)

            if escalation:
                st.warning(
                    "Human Support Recommended: "
                    "This request may need personal assistance "
                    "from the StyleHub Customer Support team."
                )

    # Save the assistant response and escalation status.
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "escalation": escalation
    })


# Sidebar information.
with st.sidebar:
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.subheader("About StyleHub")

    st.write(
        "Your online clothing store for comfortable "
        "and everyday fashion."
    )

    st.divider()

    st.write("**Customer Support Topics**")
    st.write("- Shipping and delivery")
    st.write("- Returns and refunds")
    st.write("- Payments")
    st.write("- Product information")

    st.divider()

    st.caption(
        "AI-generated answers are based on StyleHub's "
        "available company information."
    )

    st.caption(
        "Some requests may require assistance from "
        "a human support representative."
    )
