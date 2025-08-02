import streamlit as st
import os
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time

from dotenv import load_dotenv
load_dotenv()
os.environ['NVIDIA_API_KEY'] = os.getenv('NVIDIA_API_KEY')

def vector_embeddings():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = NVIDIAEmbeddings()
        st.session_state.loader = PyPDFLoader("Speech - Wikipedia.pdf")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors = FAISS.from_documents(
            st.session_state.final_documents, 
            st.session_state.embeddings
        )


st.title('Nvidia NIM Rag Chatbot')
llm = ChatNVIDIA(model="meta/llama3-70b-instruct")

prompt_template = ChatPromptTemplate.from_template(
    """
Answer the question based on the provided context only.
please provide the most accurate answer.
<context>
{context}
<context>
Questions:{input}
"""
)


prompt = st.text_input("Enter your question?")

if st.button("Documents Embedding"):
    vector_embeddings()
    st.write("Vector storw Db is ready")

if prompt:
    document_chain = create_stuff_documents_chain(llm,prompt_template)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    start = time.process_time()
    response = retrieval_chain.invoke({"input": prompt})
    st.write(response['answer'])

    with st.expander("Document Similarity search"):
        for i,doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write("------------------")