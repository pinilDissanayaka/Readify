import os
import subprocess
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain_core.documents import Document


def clone_github_repo(github_url:str, local_path:str):
    try:
        subprocess.run(['git', 'clone', github_url, local_path], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e}")
        return False

def load_repo(local_path):
    loaded_documents=DirectoryLoader(path=local_path, loader_cls=TextLoader, use_multithreading=True).load()
    
    return loaded_documents

def summary_loaded_document(documents):
    document_page_content=[]
    for document in documents:
        document_page_content.append(Document)
        
    
    

