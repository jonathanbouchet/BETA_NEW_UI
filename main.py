import os
from PIL import Image
import streamlit as st
from streamlit_image_select import image_select
from streamlit_extras.switch_page_button import switch_page
# st.set_page_config('login page', initial_sidebar_state='collapsed')

img = Image.open("assets/reflexive_ai_logo.png")
st.set_page_config(page_title="Reflexive.ai",
                   page_icon=img,
                   initial_sidebar_state="collapsed",
                   menu_items={
                       'Get Help': "mailto:support@reflexive.ai",
                       'Report a bug': "mailto:support@reflexive.ai",
                       'About': "# REFLEXIVE.AI\n ## VIRTUAL AGENTS TO HELP YOU GROW YOUR BUSINESS "
                                "\nhttps://reflexive.ai"})

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


def pretty_title(title: str) -> None:
    """Make a centered title, and give it a red line. Adapted from
    'streamlit_extras.colored_headers' package.
    Parameters:
    -----------
    title : str
        The title of your page.
    """
    st.markdown(
        f"<h2 style='text-align: center'>{title}</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        (
            '<hr style="background-color: #ff4b4b; margin-top: 0;'
            ' margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">'
        ),
        unsafe_allow_html=True,
    )


# --- Initialize session state for generated images --- #
if 'generated_image' not in st.session_state:
    st.session_state.generated_image = None


pretty_title("REFLEXIVE.AI")

# --- Placeholders for Images and Gallery --- #
generated_images_placeholder = st.empty()
gallery_placeholder = st.empty()


def app():
    # --- Gallery Display for inspiration or just plain admiration --- #
    with gallery_placeholder.container():
        index_selected = image_select(
            label="Menus",
            images=[
                "assets/Futurama-Bender-Face.jpeg", "assets/QA_logo.jpeg", "assets/chat_with_agent.png"
            ],
            captions=["Reflexive questionnaire", "Docs Q&A", "Talk with Agent"],
            use_container_width=True,
            index=-1,
            return_value="index",
        )

        st.write(index_selected)

        if index_selected == 0:
            switch_page("reflexive_questionnaire")
        elif index_selected == 1:
            switch_page("qa_doc")
        elif index_selected == 2:
            switch_page("talk_with_agent")
        else:
            st.write("This is the Home Page")


# Run the Streamlit app
if __name__ == "__main__":
    # print(f"Files and directories in {os.getcwd()}: {os.listdir(os.getcwd())}")
    for name in ["chat_messages.txt", "qa_messages.txt", "chat_messages.pdf", "qa_messages.pdf"]:
        if os.path.exists(name):
            os.remove(name)
    app()
