from graph.chains.retrieval_grader import GradeDocuments
from graph.chains.router import RouteQuery


def test_grade_documents_binary_score_accepts_yes_no() -> None:
    yes_grade = GradeDocuments(binary_score="yes")
    no_grade = GradeDocuments(binary_score="no")
    vector_route = RouteQuery(datasource="vectorstore")
    web_route = RouteQuery(datasource="websearch")

    assert yes_grade.binary_score == "yes"
    assert no_grade.binary_score == "no"
    assert vector_route.datasource == "vectorstore"
    assert web_route.datasource == "websearch"
