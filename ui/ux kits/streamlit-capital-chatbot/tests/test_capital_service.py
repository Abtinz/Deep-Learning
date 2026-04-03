"""Unit tests for CapitalChatService output normalization behavior."""

from unittest.mock import MagicMock, patch

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
        mock_chain.invoke.return_value = _FakeResponse("  Ottawa  ")

        with patch.object(CapitalChatService, "_prompt", create=True):
            service = CapitalChatService()
            service._prompt = MagicMock()
            service._prompt.__or__.return_value = mock_chain

            assert service.get_capital("Canada") == "Ottawa"


def test_get_capital_returns_fallback_on_empty_output() -> None:
    """
    Definition:
        Verify the service returns a fallback message for empty model content.

    Args:
        None

    Return:
        None
    """
    with patch("capital_service.ChatOpenAI") as mock_chat_openai:
        mock_llm = MagicMock()
        mock_chat_openai.return_value = mock_llm

        mock_chain = MagicMock()
        mock_chain.invoke.return_value = _FakeResponse("   ")

        with patch.object(CapitalChatService, "_prompt", create=True):
            service = CapitalChatService()
            service._prompt = MagicMock()
            service._prompt.__or__.return_value = mock_chain

            assert service.get_capital("Narnia") == "Unknown country."
