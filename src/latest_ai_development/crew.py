from latest_ai_development.tools.custom_tool import FileReaderTool
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class LatestAiDevelopment():
    """Job Fit Agent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def resume_profiler(self) -> Agent:
        return Agent(
    config=self.agents_config['resume_profiler'],
    tools=[FileReaderTool()],
    verbose=True
)

    @agent
    def job_extractor(self) -> Agent:
        return Agent(
    config=self.agents_config['job_extractor'],
    tools=[FileReaderTool()],
    verbose=True
)

    @agent
    def fit_scorer(self) -> Agent:
        return Agent(
            config=self.agents_config["fit_scorer"],  # must match agents.yaml key
            verbose=True
        )

    @task
    def resume_profiling_task(self) -> Task:
        return Task(
            config=self.tasks_config["resume_profiling_task"]
        )

    @task
    def job_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_extraction_task"]
        )

    @task
    def fit_scoring_task(self) -> Task:
        return Task(
            config=self.tasks_config["fit_scoring_task"]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )