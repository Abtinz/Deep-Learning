"""Gradio app for a LangChain/OpenAI country-capital chatbot."""

import os

import gradio as gr
from dotenv import load_dotenv

from capital_service import CapitalChatService


# Load environment variables once at app start.
load_dotenv()


SERVICE = None


def get_service() -> CapitalChatService:
    """
    Definition:
        Lazily initialize and return the shared capital chat service instance.

    Args:
        None

    Return:
        CapitalChatService: Initialized service instance.
    """
    global SERVICE
    if SERVICE is None:
        SERVICE = CapitalChatService()
    return SERVICE


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


def answer_capital(country: str) -> str:
    """
    Definition:
        Process user input and return the capital response string.

    Args:
        country (str): Country name submitted by the user.

    Return:
        str: Capital city or a validation/fallback message.
    """
    if not validate_environment():
        return "OPENAI_API_KEY is missing. Add it to your environment or .env file."

    cleaned_country = (country or "").strip()
    if not cleaned_country:
        return "Please enter a country name."

    return get_service().get_capital(cleaned_country)


def build_interface() -> gr.Interface:
    """
    Definition:
        Create and return the Gradio interface object for the chatbot.

    Args:
        None

    Return:
        gr.Interface: Configured Gradio interface instance.
    """
    return gr.Interface(
        fn=answer_capital,
        inputs=gr.Textbox(label="Country", placeholder="Type a country, e.g., Japan"),
        outputs=gr.Textbox(label="Capital"),
        title="Country Capital Chatbot",
        description="LangChain + OpenAI + Gradio",
    )


def main() -> None:
    """
    Definition:
        Build and launch the Gradio web application.

    Args:
        None

    Return:
        None
    """
    app = build_interface()
    server_port = int(os.getenv("GRADIO_SERVER_PORT", "7860"))
    app.launch(server_name="0.0.0.0", server_port=server_port)


if __name__ == "__main__":
    main()
