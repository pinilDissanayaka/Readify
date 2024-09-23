import os
import streamlit as st
from tempfile import TemporaryDirectory
from utils.repo_handler import clone_github_repo, load_repo, summary_loaded_document


with st.sidebar:
    st.write("This code will be printed to the sidebar.")
    
    repo_url=st.text_input("Repository URL :")
    
    temp_directory=TemporaryDirectory()
    
    with temp_directory:
        clone_status=clone_github_repo(github_url=repo_url, local_path=temp_directory.name)
        if clone_status:
            loaded_repo_data=load_repo(local_path=temp_directory.name)
            code_summaries=summary_loaded_document(documents=loaded_repo_data)
        else:
            st.error("Unexpected Error Occurred ", icon="🚨")


if code_summaries:  
    st.write(code_summaries)

