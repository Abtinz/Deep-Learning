"""Unit tests for CopilotKit-capable capital chatbot API behavior."""

from unittest.mock import patch

import app


def test_health_endpoint_shape() -> None:
    """
    Definition:
        Verify health endpoint includes key status fields for runtime checks.

    Args:
        None

    Return:
        None
    """
    response = app.health()
    assert response.status == "ok"
    assert isinstance(response.has_openai_key, bool)
    assert isinstance(response.copilotkit_available, bool)


def test_resolve_capital_requires_country() -> None:
    """
    Definition:
        Verify empty input returns a user-friendly validation message.

    Args:
        None

    Return:
        None
    """
    assert app.resolve_capital("   ") == "Please enter a country name."


def test_resolve_capital_requires_api_key() -> None:
    """
    Definition:
        Verify missing API key returns a clear setup instruction message.

    Args:
        None

    Return:
        None
    """
    with patch("app.validate_environment", return_value=False):
        assert "OPENAI_API_KEY is missing" in app.resolve_capital("Canada")


def test_resolve_capital_uses_service() -> None:
    """
    Definition:
        Verify valid requests use the shared service and return its response.

    Args:
        None

    Return:
        None
    """
    with patch("app.validate_environment", return_value=True):
        with patch("app.get_service") as mock_get_service:
            mock_get_service.return_value.get_capital.return_value = "Ottawa"
            assert app.resolve_capital("Canada") == "Ottawa"
