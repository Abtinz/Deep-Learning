"""Streamlit app for a LangChain/OpenAI country-capital chatbot."""

import os

import streamlit as st
from dotenv import load_dotenv

from capital_service import CapitalChatService


# Load environment variables once at app start.
load_dotenv()


def validate_environment() -> bool:
    """
    Definition:
        Validate that required OpenAI credentials exist before making model calls.

    Args:
        None

    Return:
        bool: True if OPENAI_API_KEY is present, else False.
    """
    return bool(os.getenv("OPENAI_API_KEY"))


def initialize_session_state() -> None:
    """
    Definition:
        Ensure Streamlit session fields exist for chat persistence.

    Args:
        None

    Return:
        None
    """
    if "messages" not in st.session_state:
        st.session_state.messages = []


def render_chat_history() -> None:
    """
    Definition:
        Render previous user and assistant messages from session storage.

    Args:
        None

    Return:
        None
    """
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_prompt(service: CapitalChatService) -> None:
    """
    Definition:
        Read user input, call the LangChain service, and append both messages.

    Args:
        service (CapitalChatService): Service object that resolves country capitals.

    Return:
        None
    """
    prompt = st.chat_input("Ask for a country's capital (e.g., Canada)")
    if not prompt:
        return

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Looking up the capital..."):
            answer = service.get_capital(prompt)
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})


def main() -> None:
    """
    Definition:
        Configure page layout and run the Streamlit chatbot workflow.

    Args:
        None

    Return:
        None
    """
    st.set_page_config(page_title="Country Capital Chatbot")
    st.title("Country Capital Chatbot")
    st.caption("LangChain + OpenAI + Streamlit")

    if not validate_environment():
        st.error("OPENAI_API_KEY is missing. Add it to your environment or .env file.")
        st.stop()

    initialize_session_state()
    render_chat_history()

    service = CapitalChatService()
    handle_user_prompt(service)


if __name__ == "__main__":
    main()
