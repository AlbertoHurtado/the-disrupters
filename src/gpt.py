import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Set org ID and API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# PROMPTS
get_intent_prompt_gpt = """
I am building an intent detector for a chatbot that help users find real estate offerings. Here are the possible options for the intent:
user_neutral_greeting
user_neutral_goodbye
user_search_properties
user_neutral_out_of_scope

What would be the right intent for this input:
“{prompt}”

Please only return the intent and nothing else. Make your answer as short as possible.
"""

def get_intent_gpt(msg):
    return get_gpt_answer(get_intent_prompt_gpt.format(prompt=msg))

def get_gpt_answer(msg):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
        messages=[{"role": "user", "content": msg}]
    )

    reply_content = completion.choices[0].message.content
    return reply_content
