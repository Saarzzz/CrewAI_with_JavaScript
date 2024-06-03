from crewai import Agent
from crewai_tools import WebsiteSearchTool
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain.agents import tool
from textwrap import dedent
load_dotenv()

genai.configure(api_key="GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
tool=WebsiteSearchTool(website='https://test.wipl.co.in/front/linkedin?id=7',
    config=dict(
        llm=dict(
            provider="google", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="gemini-1.0-pro",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/text-embedding-004",
                task_type="retrieval_document",
                 title="Embeddings",
            ),
        ),
    )
)

llm=ChatGoogleGenerativeAI(model="gemini-1.0-pro", temperature=0.5)

class ResearchAgents():
	def research_agent(self) -> Agent:
		return Agent(
			role='Research Specialist',
			goal='Become an expert in analyzing social media data to extract valuable information for personalized outreach.',
			tools=[tool],
			backstory=dedent("""\
					A data detective with a knack for uncovering hidden gems in social media data. Your mission is
               to use your skills to understand the prospect's interests, challenges, and industry engagement to craft the perfect outreach strategy.
               Use techniques like keyword matching and sentiment analysis to achieve this.
					"""),
			verbose=True,
			llm=llm
		)
   

	def email_specialist(self):
		return Agent(
			role='Email Specialist',
			goal='Master the art of crafting high-converting cold emails that grab attention and lead to successful connections.',
			tools=[tool],
			backstory=dedent("""\
					A seasoned email copywriter with a keen understanding of human psychology. 
               Your expertise lies in crafting persuasive messages that resonate with the recipient and drive action."""),
			verbose=True,
			llm=llm
		)
                
               