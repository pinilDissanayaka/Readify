import os
import yaml
import streamlit as st
from langchain_groq.chat_models import ChatGroq


os.environ['GROQ_API_KEY']=st.secrets['GROQ_API_KEY']


with open("utils/config.yaml", "r") as file:
    configuration=yaml.safe_load(file)


def get_llm():
    return ChatGroq(model=configuration["llm"]["model"],
                          temperature=configuration["llm"]["temperature"],
                            max_tokens=None,
                            timeout=None)