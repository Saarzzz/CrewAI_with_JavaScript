from datetime import datetime
from typing import Callable
from agents import ResearchAgents
from job_manager import append_event
from tasks import ResearchTasks
from crewai import Crew
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from crewai import Process
load_dotenv()

# Load the google gemini api key
genai.configure(api_key="GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class ResearchCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id
        self.crew = None
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro", temperature=0.5)

    def setup_crew(self, Context):
        agents = ResearchAgents()
        tasks = ResearchTasks(
            job_id=self.job_id)

            # Create Agents
        researcher_agent = agents.research_agent()
        #email_specialist=agents.email_specialist()

        # Create Tasks
        research = tasks.research_task(researcher_agent, Context)
        #email = tasks.email_strategy_task(email_specialist, Context, research)

        self.crew = Crew(
            agents=[
                researcher_agent
            ],
            tasks=[
                research
            ], verbose=2
        )



    def kickoff(self):
        if not self.crew:
            append_event(self.job_id, "Crew not set up")
            return "Crew not set up"

        append_event(self.job_id, "Task Started")
        try:
            results = self.crew.kickoff()
            append_event(self.job_id, "Task Complete")
            print(results)
            return results
        except Exception as e:
            append_event(self.job_id, f"An error occurred: {e}")
            return str(e)