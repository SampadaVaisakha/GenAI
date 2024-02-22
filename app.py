
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceHub
import streamlit as st

load_dotenv()

def get_huggingface_response(question):
    Hugging_Face_Hub= HuggingFaceHub(repo_id='google/flan-t5-large', model_kwargs={'temperature': 0})
    response = Hugging_Face_Hub(question)
    return response

## initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input_text = st.text_input("Input: ", key="input")
response = ""

submit = st.button("Get the Answer")

## If ask button is clicked

if submit:
    response = get_huggingface_response(input_text)
    st.subheader("The Response is")
    st.write(response)
