from .agents import MyBookWriterAgents
from .tasks import BookWriterTask
from crewai import Crew

Topic = "Artificial Intelligence"


agents = MyBookWriterAgents()
tasks = BookWriterTask()




Outline_Writer = agents.Outline_Writer()

Outline_Writer_Task = tasks.Outline_Writer_Task(
    agent = Outline_Writer,
    topic = Topic
)


crew =  Crew(
    tasks = [Outline_Writer_Task],
    agents = [Outline_Writer],
    verbose = True,
)

def BookWriter():
    results = crew.kickoff()
    print(results)