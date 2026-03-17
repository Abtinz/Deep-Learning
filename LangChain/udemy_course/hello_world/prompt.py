from langchain.prompts import PromptTemplate

summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

prompt = PromptTemplate.from_template(
        input_variables=["information"], 
        template=summary_template
)
