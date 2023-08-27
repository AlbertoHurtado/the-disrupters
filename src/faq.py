# flake8: noqa
import streamlit as st


def faq():
    st.markdown(
        """
# FAQ
## How to use App?
Here is an example conversation...

User: "I am looking for a house in Vilamoura with 3 bedrooms and 3 bathrooms"

Bot: "I have found 5 properties that match your criteria. Here is the one of the properties..."

User: "Please describe the property to me"

Bot: "Luxury tourist resort in Vilamoura, Algarve with fully furnished ..."

User: "Please show me some pictures"

Bot: "Here are some photos of the property:(shows pictures)"

User: "Show me the next property"

Bot: "Here is another property..."

## What tech stack is being uses?
The ui was built in Python using the Streamlit library. For the conversational part of the app, we are using Meta's Llama 2 through a workflow created on the Clarifai platform. We also created a demo database with information about several properties using MongoDB Atlas, but we intend on integrating a more mainstream API from a well know real estate portal, such as Idealista.

## How to test the APP?
Follow the [Github](https://github.com/AlbertoHurtado/the-disrupters) README.md to run the project locally.

"""
    )