from crewai import Agent, LLM
from tools import yt_tool
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
llm = LLM(
    model="gemma2-9b-it",provider="groq")

#create a senior blog content creator agent
blog_researcher = Agent(
    role = 'Blog Reasearcher from Youtube',
    goal = 'get the relevant video transcription for the topic {topic} from the predcited youtube channel and video',
    verbose = True,
    memory = True,
    backstory= (
        "Expert in understanding videos in Software Engineering, Cloud, Data Science, AI, and related fields and providing suggestions for blog content creation."
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation = True
)


##Create a senior blog writer agent with YT tool
blog_writer = Agent(
    role = 'Blog Writer',
    goal = 'Narrate a good understandable tech stories about the content {topic} from Youtube video',
    verbose = True,
    memory = True,
    backstory= (
        "with a flair for simplifying complex topics,you craft"
        "engaging narratives that captivate and educate, bringing new"
        'discoveries to light in an accessible manner.'

),
    llm=llm,
    tools=[yt_tool],
    allow_delegation = False
)

