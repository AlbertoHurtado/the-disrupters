# flake8: noqa
import streamlit as st


def faq():
    st.markdown(
        """
# FAQ
## How to use App?
Just describe the type of property you are looking for:

"I am looking for a house in Vilamoura with 3 bedrooms and 3 bathrooms"


## What tech stack is being uses?
The ui was built in Python using the Streamlit library. For the conversational part of the app, we are using Meta's Llama 2 through a workflow created on the Clarifai platform. We also created a demo database with information about several properties using MongoDB Atlas, but we intend on integrating a more mainstream API from a well know real estate portal, such as Idealista.

## How to test the APP?
Follow the [Github](https://github.com/AlbertoHurtado/the-disrupters) README.md to run the project locally.

"""
    )