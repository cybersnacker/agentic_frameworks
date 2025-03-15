### Playground to play with CrewAI

#### Getting Started
- Install [uv](https://github.com/astral-sh/uv) using your preferred method of installation
- Git clone this repo
- `cd <repo_name>`
- Add a `.env` file with your Language Model Provider/Tools/Integration API keys
```
OPENROUTER_API_KEY="your_key"
OPENAI_API_KEY="your_key"
ANTHROPIC_API_KEY="your_key"
SERPER_API_KEY="your_key"
```
- Run `uvx crewai run`

#### Project Structure
If you want to create your own chatbot or AI workflows, create a crewai project by running the following commands:
```
uvx crewai create crew <project_name>

cd <project_name>

Add a `.env` file with your Language Model Provider/Tools/Integration API keys

OPENROUTER_API_KEY="your_key"
OPENAI_API_KEY="your_key"
ANTHROPIC_API_KEY="your_key"
SERPER_API_KEY="your_key"

uvx crewai run
```

- Modifications to this: If you want to run crews via a python command instead of crew's crewai command, add the following code snippet to <my_project>/src/<my_project>/main.py
    ```
    if __name__ == '__main__':
    run()
    ```
    - Run `uv run src/<my_project>/main.py
    OR 
    - From the project directoy (i.e. <my_project>), run `source .venv/bin/activate` to activate the virtual environment
    - Run `python src/<my_project>/main.py`

- As you go about creating new projects/agents, feel free to write-up agent specific docs in the project's README.md

- Agents can be trained and tested 
```
uvx crewai train -n <number of iterations>. Not specifying n will default to 5 iterations
uvx crewai test
```