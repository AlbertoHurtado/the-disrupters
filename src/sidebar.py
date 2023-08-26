import streamlit as st

from src.faq import faq


def sidebar():
    with st.sidebar:
        st.markdown("# About")
        st.markdown(
            "📖 This App is template of lanchain-streamlit-docker example"
        )
        st.markdown("Made by [DR. AMJAD RAZA](https://www.linkedin.com/in/amjadraza/)")
        st.markdown("Credits for Template [hwchase17](https://github.com/hwchase17/langchain-streamlit-template)")
        st.markdown("---")

        faq()