import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Set org ID and API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response_gpt(model, session_state):

    completion = openai.ChatCompletion.create(
        model=model,
        messages=session_state['messages']
    )
    
    return completion.choices[0].message.content