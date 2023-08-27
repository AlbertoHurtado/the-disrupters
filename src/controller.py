import src.llama as llama
import src.gpt as gpt
import src.propertyFinder as propertyFinder

propertiesFound = []
current_property_idx = 0

def get_intent_from_message(prompt):
    return gpt.get_intent_gpt(prompt)

def handle_properties():
    global propertiesFound, current_property_idx
    current_property = propertiesFound[current_property_idx]

    response = f"Here is the one of the properties: {current_property['Title']}."

    if 'Location' in current_property and current_property['Location']:
        response += f" Located in {current_property['Location']}."

    if 'Bed' in current_property and current_property['Bed']:
        response += f" Has {current_property['Bed']} bedrooms."

    if 'Bath' in current_property and current_property['Bath']:
        response += f" Has {current_property['Bath']} bathrooms."

    if 'Plot' in current_property and current_property['Plot']:
        response += f" With a {current_property['Plot']} plot."

    if 'Built Area' in current_property and current_property['Built Area']:
        response += f" With a {current_property['Built Area']} build area."

    if 'Link' in current_property and current_property['Link']:
        response += f" Here is the link: {current_property['Link']}"

    return response

def get_property_images():
    global propertiesFound, current_property_idx
    current_property = propertiesFound[current_property_idx]
    images = current_property['Images']
    return images
    

def generate_response(prompt):
    global propertiesFound

    # First we get the user intent
    # We use GPT-3.5 for this because its faster
    intent = get_intent_from_message(prompt)

    if intent == "user_search_properties":
        response, propertiesFound = propertyFinder.suggestProperties(prompt)
        response += " " + handle_properties()
        result = intent, response, None
    elif intent == "user_display_property_images":
        result = intent, "Here are some photos of the property:", get_property_images()
    elif intent == "user_neutral_out_of_scope":
        result = intent, "Sorry, I can't help with that... I am a chatbot focused only on giving you recomendations on properties that we have in our database.", None
    else:
        result = intent, gpt.get_gpt_answer(prompt), None

    return result