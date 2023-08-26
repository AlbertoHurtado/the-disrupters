import src.llama as llama
import src.gpt as gpt

def get_intent_from_message(prompt):
    return gpt.get_intent_gpt(prompt)

def generate_response(prompt):
    # First we get the user intent
    # We use GPT-3.5 for this because its faster
    intent = get_intent_from_message(prompt)
    # print(intent)

    if intent == "user_search_properties":
        response = llama.generate_response_llama(prompt)
    elif intent == "user_neutral_out_of_scope":
        response = "Sorry, I can't help with that... I am a chatbot focused only on giving you recomendations on properties that we have in our database."
    else:
        response = gpt.get_gpt_answer(prompt)

    return response