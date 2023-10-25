import streamlit as st
from PIL import Image
img = Image.open("assets/QA_logo.jpeg")

st.set_page_config(page_title='Docs Q&A',
                   page_icon=img,
                   initial_sidebar_state='expanded')


st.markdown("# Docs Q&A")
st.sidebar.markdown("# Docs Q&A")
