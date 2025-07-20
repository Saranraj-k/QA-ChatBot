import streamlit as st
from langchain_groq import ChatGroq
##Tools Creation
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun, DuckDuckGoSearchRun #queryrunner
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper , DuckDuckGoSearchAPIWrapper #helps query runner

from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler


from dotenv import load_dotenv
load_dotenv()
import os

##Used the inbuilt tools
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)
##Used the inbuilt tools
api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

search = DuckDuckGoSearchRun(name='Search')

st.title("Search Engine with Tools and Agents")

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

if "messages" not in st.session_state:
    st.session_state['messages'] = [
        {"role":"assistant","content":"Hi, I am a chatbot I can serve you with the following tools: Wikipedia, Arxiv, and DuckDuckGo Search. You can ask me questions related to these topics."}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt:=st.chat_input(placeholder="WHat is Machine Learning?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key=api_key, model_name="gemma2-9b-it",streaming=True)
    tools = [wiki, arxiv, search]

    search_agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True
    )

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response = search_agent.run(
            st.session_state.messages,
            callbacks=[st_cb]
        )
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)
