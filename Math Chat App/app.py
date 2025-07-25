import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

st.set_page_config(page_title="Math Problem Solver", page_icon=":abacus:")
st.title("Text to Math Problem Solver")

groq_api_key = st.sidebar.text_input("Groq API Key", value='enter your groq api key', type="password")

if not groq_api_key:
    st.info("Please enter your Groq API Key in the sidebar to use the app.")
    st.stop()

llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")

#To search Wikipedia
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool =  Tool(
    name= "Wikipedia",
    func= wikipedia_wrapper.run,
    description="A tool for answering questions using Wikipedia, based on various topics.",
)

#To solve math
math_chain = LLMMathChain.from_llm(llm=llm)
calculator =  Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for answering math related questions. Only input mathematical expressions need to be provided."
)

prompt = """
You are a agent tasked for mathematical questions. Logically arrive at the solution and provide a detailed explanation.
and display it point wise for the question below.
question: {question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

chain = LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning",
    func=chain.run,
    description="A tool for reasoning about the question and providing a detailed explanation."
)

#Intitalize the agent with the tools
assistant_agent = initialize_agent(
    tools=[wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)


if "messages" not in st.session_state:
    st.session_state['messages'] = [
        {'role':'assistant','content':'Hi, I am a Math Chatbot to solve your Math problem'}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

question = st.text_area("Enter our question", "Tell me how 4 cranes can be used to lift 1000 kg of weight in 10 minutes.")

if st.button("Find My answer"):
    if question:
        with st.spinner("Generate response...."):
            st.session_state.messages.append({'role':'user','content':question})
            st.chat_message('user').write(question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])

            st.session_state.messages.append({'role':'assistant','content':response})
            st.write("## Response..")
            st.success(response)
    else:
        st.warning("Please enter the question")