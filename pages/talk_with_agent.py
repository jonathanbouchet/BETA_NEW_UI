import streamlit as st
from PIL import Image
img = Image.open("assets/chat_with_agent.png")

st.set_page_config(page_title='Chat with an Agent',
                   page_icon=img,
                   initial_sidebar_state='expanded')


st.markdown("# Talk with agent")
st.sidebar.markdown("# Talk with agent")
