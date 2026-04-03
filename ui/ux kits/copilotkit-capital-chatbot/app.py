"""FastAPI backend wired for CopilotKit-style chat interaction in Python."""

import os
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from capital_service import CapitalChatService


# Load environment variables once at app start.
load_dotenv()


app = FastAPI(title="CopilotKit Capital Chatbot API")
SERVICE = None
COPILOTKIT_ERROR = None

try:
    from copilotkit import Action, CopilotKitRemoteEndpoint
    from copilotkit.integrations.fastapi import add_fastapi_endpoint

    COPILOTKIT_AVAILABLE = True
except Exception as import_error:  # pragma: no cover - runtime environment dependent
    COPILOTKIT_AVAILABLE = False
    COPILOTKIT_ERROR = str(import_error)


class CapitalRequest(BaseModel):
    """Request model for country->capital lookups."""

    country: str


class CapitalResponse(BaseModel):
    """Response model for country->capital lookups."""

    capital: str


class HealthResponse(BaseModel):
    """Response model for API health endpoint."""

    status: str
    has_openai_key: bool
    copilotkit_available: bool


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


def resolve_capital(country: str) -> str:
    """
    Definition:
        Validate input and resolve the capital city with the LangChain service.

    Args:
        country (str): Country name submitted by the user.

    Return:
        str: Capital city or a fallback validation response.
    """
    cleaned_country = (country or "").strip()
    if not cleaned_country:
        return "Please enter a country name."

    if not validate_environment():
        return "OPENAI_API_KEY is missing. Add it to your environment or .env file."

    return get_service().get_capital(cleaned_country)


def copilotkit_action_handler(arguments: dict[str, Any]) -> str:
    """
    Definition:
        Handle CopilotKit action calls for country capital lookups.

    Args:
        arguments (dict[str, Any]): Action payload expected to include `country`.

    Return:
        str: Capital lookup result for the provided country.
    """
    return resolve_capital(str(arguments.get("country", "")))


def configure_copilotkit_endpoint() -> None:
    """
    Definition:
        Register the CopilotKit FastAPI endpoint when the SDK is installed.

    Args:
        None

    Return:
        None
    """
    if not COPILOTKIT_AVAILABLE:
        return

    sdk = CopilotKitRemoteEndpoint(
        actions=[
            Action(
                name="get_country_capital",
                description="Return the capital city for a given country.",
                parameters=[
                    {
                        "name": "country",
                        "type": "string",
                        "description": "Country name to resolve the capital for.",
                        "required": True,
                    }
                ],
                handler=copilotkit_action_handler,
            )
        ]
    )
    add_fastapi_endpoint(app, sdk, "/copilotkit")


configure_copilotkit_endpoint()


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """
    Definition:
        Return basic health information for quick runtime checks.

    Args:
        None

    Return:
        HealthResponse: API status, key availability, and CopilotKit status.
    """
    return HealthResponse(
        status="ok",
        has_openai_key=validate_environment(),
        copilotkit_available=COPILOTKIT_AVAILABLE,
    )


@app.post("/capital", response_model=CapitalResponse)
def capital_lookup(payload: CapitalRequest) -> CapitalResponse:
    """
    Definition:
        Fallback API endpoint for country-capital queries outside CopilotKit.

    Args:
        payload (CapitalRequest): Request body containing the country name.

    Return:
        CapitalResponse: Endpoint response with the resolved capital city.
    """
    answer = resolve_capital(payload.country)
    if answer.startswith("OPENAI_API_KEY is missing"):
        raise HTTPException(status_code=400, detail=answer)

    return CapitalResponse(capital=answer)


@app.get("/copilotkit-status")
def copilotkit_status() -> dict[str, Any]:
    """
    Definition:
        Return CopilotKit integration status and optional import error details.

    Args:
        None

    Return:
        dict[str, Any]: Availability flag and diagnostics for CopilotKit import.
    """
    return {
        "copilotkit_available": COPILOTKIT_AVAILABLE,
        "copilotkit_error": COPILOTKIT_ERROR,
    }
