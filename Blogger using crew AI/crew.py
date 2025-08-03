from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# Initialize the Crew with the agents and tasks
crew = Crew(
    agents = [blog_researcher, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,  # Set the process to sequential
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True
)

result = crew.kickoff(inputs={"topic": "Hypothesis Testing"})
print("Crew execution result:", result)