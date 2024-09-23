from langchain.prompts import ChatPromptTemplate
from utils.config import get_llm
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

llm=get_llm()

def extract_technologies(code_snippet):
    extract_technologies_prompt_template="""
        You are a code analysis assistant. Your task is to examine the provided code snippet and identify the technologies used within it.
        Analyze the following code snippet to identify the technologies and frameworks used. 
        Do not summarize the code itself. Instead, provide a list of the technologies.
        
        Code Snippet: {CODE_SNIPPET}
            
        Response Format:
            Technologies Used: [List of technologies]
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