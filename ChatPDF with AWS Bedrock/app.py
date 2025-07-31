import json
import sys
import os
import boto3
import streamlit as st

from langchain_community.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader

from langchain.vectorstores import FAISS

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQa

bedrock = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1",client=bedrock)

def data_ingestion():
    loader = PyPDFDirectoryLoader("data")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000)
    docs = text_splitter.split_documents(documents)
    return docs

def get_vector_store(docs):
    vector_store = FAISS.from_documents(
        docs,
        bedrock_embeddings
    )
    vector_store.save_local('faiss_index')

def get_claude_llm():
    llm = Bedrock(model_id = "ai21.j2.mid-v1",client=bedrock,model_kwargs={'maxTokens':512})
    return llm

def get_llama2_llm():
    llm = Bedrock(model_id = "meta.llama2-70b-chat-v1",client=bedrock,model_kwargs={'maxTokens':512})
    return llm

prompt_template = """
Human: Use the following piece of context to
provide a concise summary.
<context>
{context}
</context>
question:{question}
Assistant:
"""

prompt = PromptTemplate(
    template = prompt_template, input_variables=['context','question']
)

def get_response_llm(llm, vectorestore_faiss, query):
    qa = RetrievalQa.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=vectorestore_faiss.as_retriever(
            search_type='similarity',search_kwargs={'k':3}
        ),
        return_source_documents=True,
        chain_type_kwargs={"prompt":prompt}
    )
    answer = qa({
        'query':
        query})
    return answer['result']


def main():
    st.set_page_config('Chat PDF')
    st.header('chat with PDf using Bedrock')
    user_question = st.text_input("Ask a question from the pdf")
    with st.sidebar:
        st.title('Update or create vectore store')
        if st.button("vector_update"):
            with st.spinner("processing..."):
                docs = data_ingestion()
                get_vector_store(docs)
                st.success("Done")
    
    if st.button("claude_Output"):
        with st.spinner("processing..."):
            faiss_index = FAISS.load_local("fiass_index",bedrock_embeddings)
            llm = get_claude_llm()
            st.write(get_response_llm(llm,faiss_index,user_question))
            st.success("Done")
        
    if st.button("Llama2_Output"):
        with st.spinner("processing..."):
            faiss_index = FAISS.load_local("fiass_index",bedrock_embeddings)
            llm = get_llama2_llm()
            st.write(get_response_llm(llm,faiss_index,user_question))
            st.success("Done")

if __name__ == 'main':
    main()
        