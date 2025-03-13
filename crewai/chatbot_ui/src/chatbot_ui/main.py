#!/usr/bin/env python
import warnings

import chainlit as cl

from chatbot_ui.crew import ChatbotUi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {"message": "Loan money to a friend or help them learn how to earn money?"}

    try:
        result = ChatbotUi().crew().kickoff(inputs=inputs)
        print("Token Usage: ", result.token_usage)
        # print("Task Output: ", result.tasks_output)
        print("Raw: ", result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


@cl.on_chat_start
async def on_chat_start():
    # Create an instance of the crew
    chatbot = ChatbotUi()
    cl.user_session.set("chatbot", chatbot)
    await cl.Message(content="I'm here to give you advice. How can I help?").send()


@cl.on_message
async def on_message(message):
    message_content = message.content
    print(f"Received message from user {message_content}")
    chatbot = cl.user_session.get("chatbot")
    result = chatbot.crew().kickoff({"message": message_content})
    print(result)
    await cl.Message(content=result.raw).send()
