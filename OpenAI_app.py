import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

##LangSmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_PROJECT'] = "Q&A ChatBot with OpenAI"
os.environ['LANGCHAIN_TRACING_V2'] = "true"

##Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant"),
        ("user","Question:{question}")
    ]
)

def generate_response(question, api_key, llm, temperature, max_tokens):
    openai.api_key =  api_key
    llm = ChatOpenAI(model=llm)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question':question})
    return answer

st.title("OpenAI Q&A ChatBot")
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
## Dropdown to sleect various llm models
llm = st.sidebar.selectbox("Select an OpenAI Model", ["gpt-4-turbo", "gpt-4o",'gpt-4'])

## Slider to select temperature
temperature = st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.7)
## Slider to select max tokens
max_tokens = st.sidebar.slider("Select Max Tokens", 50, 300, 150)

st.write("Ask a question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, api_key, llm, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please provide the query!")