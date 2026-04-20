from graph.chains.retrieval_grader import GradeDocuments


def test_grade_documents_binary_score_accepts_yes_no() -> None:
    yes_grade = GradeDocuments(binary_score="yes")
    no_grade = GradeDocuments(binary_score="no")

    assert yes_grade.binary_score == "yes"
    assert no_grade.binary_score == "no"
