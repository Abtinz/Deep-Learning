"""Unit tests for Gradio capital chatbot behavior."""

from unittest.mock import MagicMock, patch

import app
from capital_service import CapitalChatService


class _FakeResponse:
    """Simple response object mimicking LangChain message content."""

    def __init__(self, content: str):
        """
        Definition:
            Create a fake response payload used in tests.

        Args:
            content (str): Content string to expose as `.content`.

        Return:
            None
        """
        self.content = content


def test_get_capital_returns_trimmed_answer() -> None:
    """
    Definition:
        Verify the service returns stripped model content when available.

    Args:
        None

    Return:
        None
    """
    with patch("capital_service.ChatOpenAI") as mock_chat_openai:
        mock_llm = MagicMock()
        mock_chat_openai.return_value = mock_llm

        mock_chain = MagicMock()
        mock_chain.invoke.return_value = _FakeResponse("  Tokyo  ")

        with patch.object(CapitalChatService, "_prompt", create=True):
            service = CapitalChatService()
            service._prompt = MagicMock()
            service._prompt.__or__.return_value = mock_chain

            assert service.get_capital("Japan") == "Tokyo"


def test_answer_capital_requires_api_key() -> None:
    """
    Definition:
        Verify API key validation blocks calls when key is missing.

    Args:
        None

    Return:
        None
    """
    with patch("app.validate_environment", return_value=False):
        message = app.answer_capital("Canada")
        assert "OPENAI_API_KEY is missing" in message


def test_answer_capital_uses_service() -> None:
    """
    Definition:
        Verify cleaned country input is sent to the service on valid requests.

    Args:
        None

    Return:
        None
    """
    with patch("app.validate_environment", return_value=True):
        with patch.object(app, "SERVICE") as mock_service:
            mock_service.get_capital.return_value = "Ottawa"

            assert app.answer_capital("  Canada  ") == "Ottawa"
            mock_service.get_capital.assert_called_once_with("Canada")
