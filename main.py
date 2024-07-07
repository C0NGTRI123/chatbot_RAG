import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from app.src.services.pdf_service import PDFService
import os
import openai

st.set_page_config(page_title="Chat", page_icon=":speech_balloon:")

with st.sidebar:
    openai_api_key = st.text_input(
        "OpenAI API Key", key="langchain_search_api_key_openai", type="password"
    )

    openai.api_key = openai_api_key


if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = [
        AIMessage(content="Xin chào tôi là trợ lý thông minh"),
    ]

st.title("Chat")

for message in st.session_state.conversation_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

user_query = st.chat_input("User: ")
if user_query is not None and user_query.strip() != "":
    st.session_state.conversation_history.append(HumanMessage(content=user_query))
    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        folder_path = r"C:\Users\congt\Desktop\test\drive-download-20240705T165934Z-001"
        file_path_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path)]
        response_conv_turn = PDFService(file_path=file_path_list,
                                        query=user_query,
                                        mode="semantic",
                                        search_rank=25,
                                        rerank_rank=3,
                                        save_path=r"C:\Users\congt\Desktop\chatbot\chatbot\dev\vector_database.index").extract()
        response = response_conv_turn
        st.markdown(response)

    st.session_state.conversation_history.append(AIMessage(content=response))
