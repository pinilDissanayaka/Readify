import os
import streamlit as st
from tempfile import TemporaryDirectory
from utils.repo_handler import clone_github_repo, load_repo, summary_loaded_document
from utils.prompt_handler import generate_readme

used_technologies=""

with st.sidebar:
    st.write("This code will be printed to the sidebar.")
    
    github_url=st.text_input("Repository URL :")
    
    temp_directory=TemporaryDirectory()
    
    if st.button("Generate"):
        with temp_directory:
            r=generate_readme(github_url=github_url)
            

st.markdown(r, unsafe_allow_html=True)
            




