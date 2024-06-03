from crewai import Task, Agent
from textwrap import dedent

from job_manager import append_event
from utils.logging import logger


class ResearchTasks():

    def __init__(self, job_id):
        self.job_id = job_id

    def append_event_callback(self, task_output):
        logger.info("Callback called: %s", task_output)
        append_event(self.job_id, task_output.exported_output)

    def research_task(self, agent, Context):
     return Task(
      description=dedent(f"""\
         Analyze the linkedin data of the prospect on linkedin to gather key points and insights, 
         focusing on information valuable for the best cold outreach.
		The Key points should be related to the my information only. Make sure to understand the date of the post. 
        Add the Post and its time in the end of each pointer as a reference. And the Pointers should be according to the context.
        Context:( {Context} )"""),
      expected_output=dedent("""key pointers of findings about the prospect, highlighting information that could be relevant for the outreach, 
                             considering the context provided. The report should be formatted in a clear and concise way, prioritizing the most valuable insights. 
                             And give the reference of the information used in the end of each pointer.
      Format:-' 
         Key Points to talk about:-
         1.  
         2.
         3.
         4.
         5.
         '
            """), agent=agent
        )

    def email_strategy_task(self,agent ,Context, research):
       return Task(
         description=dedent(f"""\
         Write a cold email for outreach to the prospect. Use the relevant key points given in the research report to draft the cold email (of approximately 70 words).
         Placeholders:
                                 [ Casestudy ]: Placeholder for a relevant case study.
                                 [ YourName ]: Placeholder for the sender's name.
                                 [ Signature ]: Placeholder for the sender's signature.
         Context: {Context}
      
         """),
         expected_output = dedent(f"""A hyper-personalized cold email (approximately 50 words) crafted by the email_specialist agent, 
                                  leveraging the key points and insights from the research report to achieve better outreach. 
                                 No pleasantries in the email.
                                 Placeholders:
                                 [ Casestudy ]: Placeholder for a relevant case study.
                                 [ YourName ]: Placeholder for the sender's name.
                                 [ Signature ]: Placeholder for the sender's signature.
                                 **Format:**
                                 ###Subject
                                 ###Body
        """),
            callback=self.append_event_callback,context=[research],
            async_execution=True,
            agent=agent
        )