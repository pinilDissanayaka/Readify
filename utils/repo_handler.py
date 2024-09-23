import os
import subprocess
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from utils.prompt_handler import extract_technologies


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
    code_summaries=[]
    for document in documents:
        code_summary=extract_technologies(code_snippet=document.page_content)
        code_summaries.append(code_summary)
        
    return code_summaries



