from prompt import prompt
from knowledgebase import information
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    llm = ChatOpenAI(
        model="gpt-5", 
        temperature=0
    )

    chain = prompt | llm

    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
