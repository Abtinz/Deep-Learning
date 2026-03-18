from prompt import prompt
from knowledgebase import information
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

def openAIChat(prompt):

    llm = ChatOpenAI(
        model="gpt-5", 
        temperature=0
    ) 

    chain = prompt | llm
    response = chain.invoke({"information": information})
    print(response.content)

def ollamaChat(prompt):

    llm = ChatOllama(
        model="gemma3:270m", 
        temperature=0
    ) 

    chain = prompt | llm
    response = chain.invoke({"information": information})

    print(response.content) 

def main():
    
    print("OpenAI Chat:")
    openAIChat(prompt)

    print("\nOllama Chat:")
    ollamaChat(prompt)



if __name__ == "__main__":
    main()
