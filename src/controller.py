import src.llama as llama
import src.gpt as gpt
import src.propertyFinder as propertyFinder

properties_found = []
current_property_idx = 0

def get_intent_from_message(prompt):
    # return gpt.get_intent_gpt(prompt)
    return llama.get_intent_llama(prompt)

def handle_properties():
    global properties_found, current_property_idx
    current_property = properties_found[current_property_idx]

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
    global properties_found, current_property_idx
    current_property = properties_found[current_property_idx]
    images = current_property['Images']
    return images

def get_property_description():
    global propertiesFound, current_property_idx
    current_property = propertiesFound[current_property_idx]
    description = current_property['description']
    gptifiedDescription = gpt.get_gpt_answer("Given this description: [DESC]"+ description + "[/DESC]. Summarize this description into less than 200 characters, to make the user want to buy this porperty.")
    return gptifiedDescription


def generate_response(prompt):
    global properties_found, current_property_idx

    # First we get the user intent
    # We use GPT-3.5 for this because its faster
    intent = get_intent_from_message(prompt)
    print(intent)

    if "user_search_properties" in intent:
        response, properties_found = propertyFinder.suggestProperties(prompt)
        current_property_idx = 0
        if len(properties_found) <= 0:
            result = intent, "Sorry, but there are no properties that fit your search.", None
        else:
            response += " " + handle_properties()
            result = intent, response, None
    elif "user_get_next_property" in intent:
        current_property_idx += 1
        print(current_property_idx)
        properties_left = len(properties_found) - current_property_idx
        if properties_left <= 0:
            result = intent, "Sorry, but there are no more properties that fit your search.", None
        else:
            response = f"There are {properties_left} properties left."
            response += " " + handle_properties()
            result = intent, response, None
    elif "user_display_property_images" in intent:
        result = intent, "Here are some photos of the property:", get_property_images()
    elif "user_requests_property_description" in intent:
        result = intent, get_property_description(), None
    elif "user_neutral_out_of_scope" in intent:
        result = intent, "Sorry, I can't help with that... I am a chatbot focused only on giving you recomendations on properties that we have in our database.", None
    else:
        result = intent, gpt.get_gpt_answer(prompt), None

    return result