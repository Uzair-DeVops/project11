from crewai import Task 
from crewai_tools import SerperDevTool , ScrapeWebsiteTool

from dotenv import load_dotenv

load_dotenv()


search_tool = SerperDevTool()
website_scrape_tool = ScrapeWebsiteTool()

class BookWriterTask():

    def Outline_Writer_Task(self , agent ,topic):
        return Task(
            description = f""" Write a detailed outline for a book on the topic search on the internet for latest data and trends on the topic and write a detailed outline for the book and also scrap the website for better data validity.
            

            Parameters:
            -----------
            topic : {topic} 
            
            """,
            tools = [search_tool,website_scrape_tool],
            agent = agent,
            expected_output = f""" A detailed outline for the book in  the format of the following
            Topic name 
            Outline:
            - Introduction
            - Chapter 1 with brief description
            - Chapter 2 with brief description
            - Chapter 3 with brief description  
            - Chapter 4 with short description
            - Chapter 5 with short description
            - Conclusion
            - References """,
        )