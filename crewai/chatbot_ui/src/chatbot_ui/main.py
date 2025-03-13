#!/usr/bin/env python
import warnings

import chainlit as cl

from chatbot_ui.crew import ChatbotUi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


# def run():
#     """
#     Run the crew.
#     """
#     inputs = {"message": "Loan money to a friend or help them learn how to earn money?"}

#     try:
#         result = ChatbotUi().crew().kickoff(inputs=inputs)
#         print("Token Usage: ", result.token_usage)
#         # print("Task Output: ", result.tasks_output)
#         print("Raw: ", result.raw)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")


# if __name__ == "main":
#     run()


@cl.on_chat_start
async def on_chat_start():
    # Create an instance of the crew
    chatbot = ChatbotUi()
    cl.user_session.set("chatbot", chatbot)
    await cl.Message(content="I'm here to give you advice. How can I help?").send()


@cl.on_message
async def main(message: cl.Message):
    chatbot = cl.user_session.get("chatbot")

    # Use cl.make_async to run the synchronous crew
    # We need to patch the step_callback to work with async
    original_callback = chatbot.custom_step_callback

    # Create a wrapper to handle the async callback
    def sync_callback(agent_finish):
        # This will run the async function and return immediately
        cl.run_sync(original_callback(agent_finish))

    # Replace the callback temporarily
    chatbot.custom_step_callback = sync_callback

    # Run the crew and send the final result
    await cl.Message(content=f"Starting crew with input: {message.content}").send()

    # Execute the crew
    await cl.make_async(chatbot.crew().kickoff)({"message": message.content})

    # Send the final result
    # await cl.Message(content=f"## Final Result\n\n{result}").send()
