### Hyper Personalized Cold Emails for the Linkedin Prospects or Leads. ###

This is a repository for the Crew AI agents with full stack development using JS(Basic).

This repository contains Python code for a set of tasks that can be used to automate outreach processes. The primary focus is on cold email outreach, leveraging LinkedIn data to personalize emails for improved results.

### Functionalities
The code defines two main functionalities:

Research Task: Analyzes a prospect's LinkedIn data to gather key points and insights relevant for crafting a compelling cold email.
Email Strategy Task: Generates a hyper-personalized cold email based on the findings from the research task.
Code Breakdown
tasks.py: This file contains the core implementation of the functionalities mentioned above.
ResearchTasks class:
research_task: This function defines the task for analyzing LinkedIn data. It takes the agent and context as input and returns a Task object specifying the description, expected output, and the agent responsible for execution.
email_strategy_task: This function defines the task for generating a cold email. It takes the agent, context, and research output as input and returns a Task object specifying the description, expected output, callback function for post-processing, context (including the research results), and the agent responsible for execution.

#### How to run:-
Run api.py file in the CrewAI folder to start the local server for testing and Open index.html given in the JS Folder.
####

Note: This readme provides a general overview of the functionalities.
