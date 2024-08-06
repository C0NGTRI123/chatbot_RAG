import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Hỏi và đáp", page_icon=":speech_balloon:")

height = 120
logo = "https://www.pixenli.com/image/fm0aEpMI"

st.markdown(
    f"""
    <style>
        [data-testid="stSidebarNav"] {{
            background-image: url({logo});
            background-repeat: no-repeat;
            padding-top: {height - 40}px;
            background-position: 20px 20px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


# with st.sidebar:
#     st.image("https://www.pixenli.com/image/fm0aEpMI", width=150)
