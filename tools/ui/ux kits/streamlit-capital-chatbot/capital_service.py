"""Core LangChain service for answering country capital questions."""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class CapitalChatService:
    """LangChain wrapper that asks OpenAI for country capitals only."""

    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.0) -> None:
        """
        Definition:
            Initialize the chatbot service with a deterministic OpenAI chat model.

        Args:
            model_name (str): OpenAI model name used by LangChain ChatOpenAI.
            temperature (float): Sampling temperature for the model response.

        Return:
            None
        """
        self._llm = ChatOpenAI(model=model_name, temperature=temperature)
        self._prompt = ChatPromptTemplate.from_template(
            """
You are a precise geography assistant.
Return only the capital city for the country the user provides.
If the input is not a valid country, return: Unknown country.
Do not add extra words.

Country: {country}
            """.strip()
        )

    def get_capital(self, country: str) -> str:
        """
        Definition:
            Ask the LangChain pipeline for the capital city of a given country.

        Args:
            country (str): Name of the country entered by the user.

        Return:
            str: The model's capital city answer or a fallback message.
        """
        # Compose a prompt+model chain and invoke it with the user's country input.
        chain = self._prompt | self._llm
        response = chain.invoke({"country": country.strip()})

        # Normalize and return a safe plain-text result for UI rendering.
        answer = (response.content or "").strip()
        return answer if answer else "Unknown country."
