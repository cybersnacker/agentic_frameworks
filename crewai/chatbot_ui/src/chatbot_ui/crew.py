import chainlit as cl
from crewai_tools import SerperDevTool

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


def on_task_complete(task_result):
    print("Task Result from callback: ", task_result)


@CrewBase
class ChatbotUi:
    """ChatbotUi crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    async def custom_step_callback(self, agent_finish):
        """
        Step callback function for the angel agent

        Parameters:
            agent: The agent executing the step
        """
        print("Yay! Inside agent callback function")
        # Extract information
        thought = getattr(agent_finish, "thought", None)
        output = getattr(agent_finish, "output", None)
        # tool = getattr(agent_finish, "tool", None)

        transparent_content = ""

        if thought:
            print(f"Thought: {thought}")
            transparent_content += f"**Thought**: {thought}\n"

        # if tool:
        #     print(f"Tool: {tool}")
        #     transparent_content += f"**Tool**: {tool}\n"

        if output:
            print(f"Output: {output}")
            transparent_content += f"**Output**: {output}\n"

        await cl.Message(content=transparent_content).send()

        # return agent_finish
        # print("Agent txt: ", agent_finish.text)

    @agent
    def angel(self) -> Agent:
        return Agent(
            config=self.agents_config["angel"],
            allow_delegation=False,
            tools=[SerperDevTool()],
        )

    @agent
    def badass(self) -> Agent:
        return Agent(
            config=self.agents_config["badass"],
            allow_delegation=False,
        )

    @task
    def task1(self) -> Task:
        return Task(config=self.tasks_config["task1"])  # callback=on_task_complete)

    @task
    def task2(self) -> Task:
        return Task(config=self.tasks_config["task2"])  # callback=on_task_complete)

    @crew
    def crew(self) -> Crew:
        """Creates the ChatbotUi crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            step_callback=self.custom_step_callback,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

    ### Figure out what is being passed to step_callback
    # def debug_callback(*args, **kwargs):
    #     """
    #     A wrapper callback that logs all arguments passed to it
    #     This can be used to understand what parameters CrewAI is passing
    #     """
    #     try:
    #         # Log the number and type of arguments
    #         print(
    #             f"Callback received {len(args)} positional arguments and {len(kwargs)} keyword arguments"
    #         )

    #         # Log information about each positional argument
    #         for i, arg in enumerate(args):
    #             print(f"Positional arg {i}: type={type(arg).__name__}")

    #         # Log each keyword argument
    #         for key, value in kwargs.items():
    #             print(f"Keyword arg '{key}': type={type(value).__name__}")

    #             # For string or simple types, show the value
    #             if isinstance(value, (str, int, float, bool)) or value is None:
    #                 print(f"Value of '{key}': {value}")

    #         # Inspect the call stack to see what function called this callback
    #         caller_frame = inspect.currentframe().f_back
    #         if caller_frame:
    #             caller_info = inspect.getframeinfo(caller_frame)
    #             print(
    #                 f"Called from: {caller_info.filename}:{caller_info.lineno} in {caller_info.function}"
    #             )
    #     except Exception as e:
    #         print(e)
