"""FastAPI backend for country-capital chat interactions in Python."""

import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from capital_service import CapitalChatService


# Load environment variables once at app start.
load_dotenv()


app = FastAPI(title="Capital Chatbot API")
SERVICE = None


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


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """
    Definition:
        Return basic health information for quick runtime checks.

    Args:
        None

    Return:
        HealthResponse: API status and key availability.
    """
    return HealthResponse(
        status="ok",
        has_openai_key=validate_environment(),
    )


@app.post("/capital", response_model=CapitalResponse)
def capital_lookup(payload: CapitalRequest) -> CapitalResponse:
    """
    Definition:
        API endpoint for country-capital queries.

    Args:
        payload (CapitalRequest): Request body containing the country name.

    Return:
        CapitalResponse: Endpoint response with the resolved capital city.
    """
    answer = resolve_capital(payload.country)
    if answer.startswith("OPENAI_API_KEY is missing"):
        raise HTTPException(status_code=400, detail=answer)

    return CapitalResponse(capital=answer)
