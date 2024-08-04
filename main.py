import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from app.src.services.pdf_service import PDFService
import openai

st.set_page_config(page_title="Chat", page_icon=":speech_balloon:")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = [
        AIMessage(content="Xin chào tôi là trợ lý thông minh"),
    ]

st.title("Chat")

for message in st.session_state.conversation_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content.replace("\n", "<br>"), unsafe_allow_html=True)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

user_query = st.chat_input("User: ")
if user_query is not None and user_query.strip() != "":
    st.session_state.conversation_history.append(HumanMessage(content=user_query))
    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        file_path_list = []
        response_conv_turn = PDFService(file_path=file_path_list,
                                        query=user_query,
                                        mode="semantic",
                                        search_rank=25,
                                        rerank_rank=3,
                                        save_path="vector_database.index").extract()

        response = response_conv_turn
        st.markdown(response.replace("\n", "<br>"), unsafe_allow_html=True)

    st.session_state.conversation_history.append(AIMessage(content=response))
