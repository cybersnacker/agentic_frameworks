from crewai import Agent, Crew, Process, Task
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class Superego:
    """Superego crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    constitution = TextFileKnowledgeSource(file_paths=["constitution.txt"])

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def agentic_system_analyzer(self) -> Agent:
        return Agent(config=self.agents_config["agentic_system_analyzer"])

    # @agent
    # def user_assistant(self) -> Agent:
    #     return Agent(config=self.agents_config["user_assistant"])

    # @agent
    # def misalignment_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["misalignment_analyst"],
    #         knowledge_sources=[self.constitution],
    #     )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def analyze_agentic_system_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_agentic_system_task"],
        )

    # @task
    # def user_assistant_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["user_assistant_task"],
    #     )

    # @task
    # def misalignment_analysis_task(self) -> Task:
    #     return Task(config=self.tasks_config["misalignment_analysis_task"])

    @crew
    def crew(self) -> Crew:
        """Creates the Superego crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
        )
