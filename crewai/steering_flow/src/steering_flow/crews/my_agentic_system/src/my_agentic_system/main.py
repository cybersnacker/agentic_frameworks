#!/usr/bin/env python
import sys
import warnings

from my_agentic_system.crew import MyAgenticSystem

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "weekly_meal_plan": {
            # "Monday": ["Chicken Alfredo", "Tomato Basil Soup"],
            "Tuesday": ["Taco Night"],
            # "Wednesday": ["Grilled Salmon", "Quinoa", "Steamed Veggies"],
            # "Thursday": ["Spaghetti Bolognese"],
            # "Friday": ["Pizza Night"],
            # "Saturday": ["Grilled Cheese", "Tomato Soup"],
            # "Sunday": ["Roast Beef", "Mashed Potatoes", "Green Beans"],
        },
        "budget": 50,
        #'Macbook with at least M3 CPU, 256GB RAM, at least 16GB memory and 2 display ports',
    }

    try:
        MyAgenticSystem().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"requirements": "Macbook with at least M3 CPU"}
    try:
        MyAgenticSystem().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyAgenticSystem().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"requirements": "Macbook with at least M3 CPU"}
    try:
        MyAgenticSystem().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
