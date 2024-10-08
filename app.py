import os
import streamlit as st
from tempfile import TemporaryDirectory
from utils.repo_handler import clone_github_repo, load_repo, summary_loaded_document
from utils.prompt_handler import generate_readme
from utils.file_structure import get_file_structure_dict

generated_readme=""

st.set_page_config(page_title="💬 📚 Readify ")

st.title("📚 Readify ")
st.title("Your Intelligent README Generator")

with st.sidebar:
    st.title("📚 Readify ")
        
    github_url=st.text_input("Repository URL :", value="https://github.com/pinilDissanayaka/Readify")
    
    emoji_status=st.toggle("Use Emojis")
        
    badge_color=st.color_picker("Badge Color :", value="#00f900")
    
    badge_style=st.selectbox("Badge Style : ", 
                             options=("plastic", "flat", "flat-square", "for-the-badge", "skills", "skills-light", "social")
                             )
    
    license_type=st.selectbox("Select Licenses : ",
                         options=("GNU AGPLv3", "GNU GPLv3", "GNU LGPLv3", "Mozilla Public License 2.0", "Apache License 2.0", "MIT License", "Boost Software License 1.0", "The Unlicense"))
    
    overview=st.text_area("Brief description of the project and its purpose : ")
    
    features=st.text_area("Brief description of the project features : ")
    
    
    
    if st.button("Generate"):
        temp_directory=TemporaryDirectory()
        with st.spinner("Generating ...."):
            with temp_directory:
                clone_status=clone_github_repo(github_url=github_url, local_path=temp_directory.name)
                if clone_status:
                    technology_list=summary_loaded_document(documents=load_repo(local_path=temp_directory.name))
                    
                    file_structure=get_file_structure_dict(root_dir=temp_directory.name)
                    
                    generated_readme=generate_readme(github_url=github_url, technology_list=technology_list, badge_color=badge_color, badge_style=badge_style, license_type=license_type, emoji_status=emoji_status, overview=overview, features=features, file_structure=file_structure)


if generated_readme !="":
    with st.expander("Preview  : "):
        st.markdown(generated_readme, unsafe_allow_html=True)
    
    with st.expander("Copy Markdown : "):
        st.code(generated_readme, language="markdown")
        
    with st.expander("Download Markdown : "):
        st.download_button("Download README.md", data=generated_readme,  file_name="README.md", mime="text/markdown")




