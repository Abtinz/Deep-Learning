from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""

    binary_score: Literal["yes", "no"] = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )

system = """You are a grader assessing relevance of a retrieved document to a user question. \n 
    If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant. \n
    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""

grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Retrieved document: \n\n {document} \n\n User question: {question}"),
    ]
)


class _LazyRetrievalGrader:
    def __init__(self) -> None:
        self._chain = None

    def _build_chain(self):
        llm = ChatOpenAI(model="gpt-4", temperature=0)
        structured_llm_grader = llm.with_structured_output(GradeDocuments)
        return grade_prompt | structured_llm_grader

    def invoke(self, payload: dict) -> GradeDocuments:
        if self._chain is None:
            self._chain = self._build_chain()
        return self._chain.invoke(payload)


retrieval_grader = _LazyRetrievalGrader()
