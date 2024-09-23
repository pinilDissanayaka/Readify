from langchain.prompts import ChatPromptTemplate

extract_technologies_prompt_template="""
    You are a code analysis assistant. Your task is to examine the provided code snippet and identify the technologies used within it.
    Analyze the following code snippet to identify the technologies and frameworks used. 
    Do not summarize the code itself. Instead, provide a list of the technologies, 
    and if there are any special features or unique implementations within the code, summarize those briefly.
        Code Snippet: {CODE_SNIPPET}
        
        Response Format:

            Technologies Used: [List of technologies]
            Special Features: [Brief summary of any unique implementations]
    """

extract_technologies_prompt=ChatPromptTemplate.from_template(template=extract_technologies_prompt_template)


