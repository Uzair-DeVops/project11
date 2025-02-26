from .agents import MyBookWriterAgents
from .tasks import BookWriterTask
from crewai import Crew

def writer(data):
    agents = MyBookWriterAgents()
    tasks = BookWriterTask()

    Book_Writer = agents.Book_Writer()
    Book_Writer_Task = tasks.Book_Writer_Task(
        agent=Book_Writer,
        outline=data
    )

    crew = Crew(
        tasks=[Book_Writer_Task],
        agents=[Book_Writer],
        verbose=True,
    )

    result = crew.kickoff()
    print(result)
    return result  # Return the result for further use
