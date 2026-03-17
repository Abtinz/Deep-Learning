from langchain import OpenAIChat
from prompt import prompt
from knowledgebase import information


def main():

    llm = OpenAIChat(
        model="gpt-5", 
        temperature=0
    )

    print(prompt)

    chain = prompt | llm

    print(chain)

    response = chain(information=information)

    print(response)

if __name__ == "__main__":
    main()
