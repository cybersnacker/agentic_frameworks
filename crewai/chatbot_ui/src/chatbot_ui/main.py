#!/usr/bin/env python
import warnings

import chainlit as cl

from chatbot_ui.crew import ChatbotUi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


# def run():
#     """
#     Run the crew.
#     """
#     inputs = {"topic": "AI LLMs", "current_year": str(datetime.now().year)}

#     try:
#         ChatbotUi().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {"topic": "AI LLMs"}
#     try:
#         ChatbotUi().crew().train(
#             n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
#         )

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")


# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         ChatbotUi().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")


# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {"topic": "AI LLMs", "current_year": str(datetime.now().year)}
#     try:
#         ChatbotUi().crew().test(
#             n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
#         )

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")


@cl.on_chat_start
async def on_chat_start():
    chatbot = ChatbotUi()
    cl.user_session.set("chatbot", chatbot)
    await cl.Message(content="Hey buddy, what's up?").send()


@cl.on_message
async def on_message(message):
    message_content = message.content
    print(f"Received message from user {message_content}")
    chatbot = cl.user_session.get("chatbot")
    result = chatbot.crew().kickoff({"message": message_content})
    await cl.Message(content=result.raw).send()
