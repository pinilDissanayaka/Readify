from langchain.prompts import ChatPromptTemplate
from utils.config import get_llm
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

llm=get_llm()

def extract_technologies(code_snippet):
    extract_technologies_prompt_template="""
        You are a code analysis assistant. Your task is to examine the provided code snippet and identify the most used languages and frameworks used within it.
        Analyze the following code snippet to identify the languages and frameworks used. 
        Do not summarize the code itself. Instead, provide a list of the languages and frameworks.
        
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
        You are a code analysis assistant. Your task is to examine the provided list and identify the final languages and frameworks used within it.
        I have a list of languages and frameworks mentioned below. Identify all the languages and frameworks that have been used or are relevant in this context:

        {LIST_OF_TECHNOLOGIES}

        Please provide the names of the languages and frameworks from the list."
            
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


def generate_readme(github_url, technology_list, badge_color, badge_style, license_type, emoji_status):
    if emoji_status:
        readme_generate_prompt_template="""
            You are an expert at creating professional GitHub README files. 
            Generate a comprehensive README file for a GitHub project. 
            Use the following structure and fill in the relevant sections based on the given information and 
            the GitHub repository at the provided URL:

            Title and Description:
                Brief description of the project and its purpose.
            
            Badges:
                Include badges for license, last commit, top language, and language count.
                make this badges with shields.io icons and logos.
                and use {BADGE_COLOR} as a badge color and {BADGE_STYLE} as a badge style.
                    
            Built With:
                List the technologies and tools used in the project with appropriate badges.
                used languages and frame works : {TECHNOLOGY_LIST}
                make this badges with shields.io icons and logos. and use {BADGE_COLOR} as a badge color and {BADGE_STYLE} as a badge style.
                
            Table of Contents:
            Include a table of contents linking to the following sections:
                Overview
                Features
                Repository Structure
                Modules
                Getting Started
                Prerequisites
                Installation
                Usage
                Project Roadmap
                Contributing
                License
                Acknowledgments
                
            Overview:
                Provide a brief overview of the project.
            
            Features:
                Highlight key features of the project.
                
            Repository Structure:
                Include a visual representation of the project structure.
            
            Modules:
                List the main modules/files with a brief summary of their purpose.
                
            Getting Started:
                Provide instructions for prerequisites, installation steps, and how to run the project.
                This section make a bash commands. 

            Project Roadmap:
                Outline future plans for the project.
                
            Contributing:
                Explain how others can contribute to the project.
                The section should include:
                    Report Issues: Instructions for users to submit bugs found or log feature requests.
                    Submit Pull Requests: Guidance on how to review open pull requests and submit their own.
                    Join the Discussions: Information on how users can participate in community discussions.
                Make sure to include relevant links to the issue tracker, pull requests, and discussions pages of the repository.
                Generate an HTML snippet to display the contributor tree for the GitHub repository at the given URL. 
                Include an image that links to the repository's contributors page.
                
            License:
                State the license under which the project is released.
                {LICENSE_TYPE}
            
            Acknowledgments:
                Credit any resources, contributors, or inspirations.
                
            GitHub URL: {GITHUB_URL}
            
            Finally make this readme file interactively using emoji at the many places.
        """
        
        readme_generate_prompt=ChatPromptTemplate.from_template(template=readme_generate_prompt_template)
        
        readme_generate_chain=(
            {"GITHUB_URL" : RunnablePassthrough(), "TECHNOLOGY_LIST" : RunnablePassthrough(), "BADGE_COLOR": RunnablePassthrough(), "BADGE_STYLE": RunnablePassthrough(), "LICENSE_TYPE": RunnablePassthrough()} |
            readme_generate_prompt |
            llm |
            StrOutputParser()
        )
        
        generated_readme=readme_generate_chain.invoke({"GITHUB_URL" : github_url, "TECHNOLOGY_LIST": technology_list, "BADGE_COLOR" :badge_color, "BADGE_STYLE":badge_style, "LICENSE_TYPE" : license_type})
    
    else:
        readme_generate_prompt_template="""
        You are an expert at creating professional GitHub README files. 
        Generate a comprehensive README file for a GitHub project. 
        Use the following structure and fill in the relevant sections based on the given information and 
        the GitHub repository at the provided URL:

        Title and Description:
            Brief description of the project and its purpose.
        
        Badges:
            Include badges for license, last commit, top language, and language count.
            make this badges with shields.io icons and logos.
            and use {BADGE_COLOR} as a badge color and {BADGE_STYLE} as a badge style.
                
        Built With:
            List the technologies and tools used in the project with appropriate badges.
            used languages and frame works : {TECHNOLOGY_LIST}
            make this badges with shields.io icons and logos. and use {BADGE_COLOR} as a badge color and {BADGE_STYLE} as a badge style.
            
        Table of Contents:
        Include a table of contents linking to the following sections:
            Overview
            Features
            Repository Structure
            Modules
            Getting Started
            Prerequisites
            Installation
            Usage
            Project Roadmap
            Contributing
            License
            Acknowledgments
            
        Overview:
            Provide a brief overview of the project.
        
        Features:
            Highlight key features of the project.
            
        Repository Structure:
            Include a visual representation of the project structure.
        
        Modules:
            List the main modules/files with a brief summary of their purpose.
            
        Getting Started:
            Provide instructions for prerequisites, installation steps, and how to run the project.

        Project Roadmap:
            Outline future plans for the project.
            
        Contributing:
            Explain how others can contribute to the project.
            The section should include:
                Report Issues: Instructions for users to submit bugs found or log feature requests.
                Submit Pull Requests: Guidance on how to review open pull requests and submit their own.
                Join the Discussions: Information on how users can participate in community discussions.
            Make sure to include relevant links to the issue tracker, pull requests, and discussions pages of the repository.
            Generate an HTML snippet to display the contributor tree for the GitHub repository at the given URL. 
            Include an image that links to the repository's contributors page.
            
        License:
            State the license under which the project is released.
            {LICENSE_TYPE}
        
        Acknowledgments:
            Credit any resources, contributors, or inspirations.
            
        GitHub URL: {GITHUB_URL}
        
        Finally make this readme file interactively without using emoji.
    """
    
    readme_generate_prompt=ChatPromptTemplate.from_template(template=readme_generate_prompt_template)
    
    readme_generate_chain=(
        {"GITHUB_URL" : RunnablePassthrough(), "TECHNOLOGY_LIST" : RunnablePassthrough(), "BADGE_COLOR": RunnablePassthrough(), "BADGE_STYLE": RunnablePassthrough(), "LICENSE_TYPE": RunnablePassthrough()} |
        readme_generate_prompt |
        llm |
        StrOutputParser()
    )
    
    generated_readme=readme_generate_chain.invoke({"GITHUB_URL" : github_url, "TECHNOLOGY_LIST": technology_list, "BADGE_COLOR" :badge_color, "BADGE_STYLE":badge_style, "LICENSE_TYPE" : license_type})
    
    return generated_readme



