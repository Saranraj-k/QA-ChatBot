import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
import os


## app
st.set_page_config(page_title="LangChain:Summarize Text from YT or website", page_icon=":books:")
st.title("LangChain: Summarize Text from YouTube or Website")
st.subheader("Summarize URL")                   



with st.sidebar:
    groq_api_key = st.text_input("Groq API Key",value='enter your groq api key', type="password")

url = st.text_input('URL',label_visibility='collapsed')

llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")

prompt_template = """
please summarize the following text in a concise manner.
content:{text}
summary:
"""

prompt = PromptTemplate(
    input_variables=["text"],
    template=prompt_template
)

final_prompt_temp = '''
Provide the final summary of the entire documents with the important points.
content: {text}'''

final_prompt = PromptTemplate(
    input_variables=["text"],
    template=final_prompt_temp
)


if st.button("Summarize the content from YT or Website"):
    if not groq_api_key.strip() or not url.strip():
        st.error("Please enter a valid Groq API Key and URL.")
    elif not validators.url(url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Waiting.."):
                if "youtube.com" in url:
                    loader = YoutubeLoader.from_youtube_url(url)
                else:
                    loader =  UnstructuredURLLoader(urls=[url],ssl_verify=False,
                                                    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"})
                docs = loader.load()

                chain = load_summarize_chain(llm,chain_type='map_reduce',map_prompt=prompt,combine_prompt=final_prompt)
                summary = chain.run(docs)
                st.write(summary)
        except Exception as e:
            st.exception(f"Exception:{e}")