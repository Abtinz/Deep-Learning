from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class GradeAnswer(BaseModel):
    binary_score: bool = Field(
        description="Answer addresses the question: true for yes, false for no."
    )


llm = ChatOpenAI(temperature=0)
structured_llm_grader = llm.with_structured_output(GradeAnswer)

system = """You are a grader assessing whether an answer addresses/resolves a question.
Give a binary score 'yes' or 'no'. 'yes' means the answer resolves the question."""
answer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "User question:\n\n{question}\n\nLLM generation: {generation}"),
    ]
)

answer_grader = answer_prompt | structured_llm_grader
