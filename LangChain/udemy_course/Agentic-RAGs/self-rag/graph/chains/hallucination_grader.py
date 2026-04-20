from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class GradeHallucinations(BaseModel):
    """Binary score for whether generation is grounded in documents."""

    binary_score: bool = Field(
        description="Answer is grounded in facts: true for yes, false for no."
    )


llm = ChatOpenAI(temperature=0)
structured_llm_grader = llm.with_structured_output(GradeHallucinations)

system = """You are a grader assessing whether an LLM generation is grounded in a set of retrieved facts.
Give a binary score 'yes' or 'no'. 'yes' means the answer is grounded in the facts."""
hallucination_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Set of facts:\n\n{documents}\n\nLLM generation: {generation}"),
    ]
)

hallucination_grader = hallucination_prompt | structured_llm_grader
