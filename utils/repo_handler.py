import os
import subprocess
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.prompt_handler import extract_technologies, get_technology_set


def clone_github_repo(github_url:str, local_path:str):
    try:
        subprocess.run(['git', 'clone', github_url, local_path], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e}")
        return False

def load_repo(local_path):
    loaded_documents=DirectoryLoader(path=local_path, loader_cls=TextLoader, use_multithreading=True, silent_errors=True).load_and_split()
    
    return loaded_documents

def summary_loaded_document(documents):
    list_of_technologies=[]
    
    spited_documents=RecursiveCharacterTextSplitter(chunk_size=1200,
        chunk_overlap=390,
        length_function=len,
        is_separator_regex=False).split_documents(documents=documents)
    
    for spited_document in spited_documents:
        code_summary=extract_technologies(code_snippet=spited_document.page_content)
        list_of_technologies.append(code_summary)
    
    technologies=get_technology_set(list_of_technologies=list_of_technologies)
        
    return technologies



