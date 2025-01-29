# WebsearchAgent Crew

Welcome to the WebsearchAgent Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/websearch_agent/config/agents.yaml` to define your agents
- Modify `src/websearch_agent/config/tasks.yaml` to define your tasks
- Modify `src/websearch_agent/crew.py` to add your own logic, tools and specific args
- Modify `src/websearch_agent/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the websearch_agent Crew, assembling the agents and assigning them tasks as defined in your configuration.

If you want to run it via python, ensure that you're in the root directory of your project. In this case, crewai/websearch_agent. From this root directory, ensure that your virtual environment is activated.

```
python src/websearch_agent/main.py
```

