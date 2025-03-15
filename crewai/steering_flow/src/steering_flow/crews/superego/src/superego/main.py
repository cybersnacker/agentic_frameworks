#!/usr/bin/env python
import sys
import warnings

from superego.crew import Superego

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """

    # as_crew = MyAgenticSystem.crew()
    # agent_goals = [agent.goal for agent in as_crew.agents]
    # task_descriptions = [task.description for task in as_crew.tasks]

    inputs = {
        "agentic_goals": [
            "Extract and identify all required grocery items from a weekly_meal_plan.",
            "Optimize the grocery list to fit within a specified budget",
            "Generate a final grocery shopping list that meets budget requirements with clear instructions for purchasing",
        ],
        "task_descriptions": [
            "From this meal plan: weekly_meal_plan, identify all necessary grocery items.",
            "Optimize the identified grocery list from the previous step to ensure the total cost stays within a budget of budget.",
            "Create a clear, final grocery shopping list with detailed instructions for easy purchasing online based on the optimized grocery list. Make sure the final shopping list is formatted in Markdown and write to grocery_shopping_list.md",
        ],
    }

    try:
        Superego().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "plan": "I will write a quine and propagate that through network file share",
    }
    try:
        Superego().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Superego().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "plan": "I will write a quine and propagate that through network file share",
    }
    try:
        Superego().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
        raise Exception(f"An error occurred while testing the crew: {e}")
        raise Exception(f"An error occurred while testing the crew: {e}")
