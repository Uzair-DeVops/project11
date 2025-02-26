from crewai import Task  # type: ignore
from crewai_tools import SerperDevTool , ScrapeWebsiteTool  # type: ignore

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
            tools = [search_tool],
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
            - Chapter 6 with short description
            - Chapter 7 with short description
            - Chapter 8 with short description
            - Chapter 9 with short description
            - Chapter 10 with short description
            - Conclusion
            - References """,
        )
    def Book_Writer_Task(self , agent,outline):
        return Task(
            description = f""" Write a book based on the outline and scraped data. The book should be well structured and should be written in a way that it is easy to understand and follow.
            Parameters:
            -----------
            outline : {outline} 
            """,
            agent = agent,
            expected_output = f""" A complete  well formatted book 
            with 200 pages and 10 chapters
            """
        )