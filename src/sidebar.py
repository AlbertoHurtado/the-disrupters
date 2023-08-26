import streamlit as st

from src.faq import faq


def sidebar():
    with st.sidebar:
        st.markdown("# RECA - a real estate conversational agent 🏘️")
        st.markdown("# About")
        st.markdown(
            "📖 This App was created for LabLabAi's Llama 2 Hackathon with Clarifai."
        )
        st.markdown(
            "This conversational agent take a user's description of their ideal home and finds the best results in our database and returns a detailed description of the property."
        )
        st.markdown("Made by [Alberto Hurtado](https://github.com/AlbertoHurtado) & [João Pedro Soares](https://github.com/jpssoares).")
        st.markdown("---")

        faq()