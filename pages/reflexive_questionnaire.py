import streamlit as st
from PIL import Image
img = Image.open("assets/Futurama-Bender-Face.jpeg")

st.set_page_config(page_title='Reflexive questionnaire',
                   page_icon=img,
                   initial_sidebar_state='expanded')

st.markdown("# Reflexive Questionnaire")
st.sidebar.markdown("# Reflexive Questionnaire")
