from langchain.prompts import ChatPromptTemplate
from utils.config import get_llm
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

llm=get_llm()

def extract_technologies(code_snippet):
    extract_technologies_prompt_template="""
        You are a code analysis assistant. Your task is to examine the provided code snippet and identify the most used technologies used within it.
        Analyze the following code snippet to identify the technologies and frameworks used. 
        Do not summarize the code itself. Instead, provide a list of the technologies.
        
        Code Snippet: {CODE_SNIPPET}
            
        Response Format:
            [List of technologies]
        """

    extract_technologies_prompt=ChatPromptTemplate.from_template(template=extract_technologies_prompt_template)


    extract_technologies_chain=(
        {"CODE_SNIPPET": RunnablePassthrough()} |
        extract_technologies_prompt |
        llm |
        StrOutputParser()
    )

    extract_technologies=extract_technologies_chain.invoke({"CODE_SNIPPET": code_snippet})
    
    return extract_technologies


def get_technology_set(list_of_technologies):
    get_technology_set_prompt_template="""
        You are a code analysis assistant. Your task is to examine the provided technology list and identify the final technologies used within it.
        I have a list of technologies mentioned below. Identify all the technologies that have been used or are relevant in this context:

        {LIST_OF_TECHNOLOGIES}

        Please provide the names of the technologies from the list."
            
        Response Format:
            [List of technologies]
        """

    get_technology_set_prompt=ChatPromptTemplate.from_template(template=get_technology_set_prompt_template)


    extract_technologies_chain=(
        {"LIST_OF_TECHNOLOGIES": RunnablePassthrough()} |
        get_technology_set_prompt |
        llm |
        StrOutputParser()
    )

    extract_technologies=extract_technologies_chain.invoke({"LIST_OF_TECHNOLOGIES": list_of_technologies})
    
    return extract_technologies
    