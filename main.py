import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from app.src.services.pdf_service import PDFService
import openai

# Create a css style for the chatbot
center_elements_css = """
<style>
.centered-element {
  text-align: center;
}
</style>
"""

left_elements_css = """
<style>
.left-element {
  text-align: left;
}
</style>
"""

right_elements_css = """
<style>
.right-element {
  text-align: right;
}
</style>
"""

html = """
<style>
.top-left-image {
    position: absolute;
    top: -60px;
    left: -300px;
    z-index: 1;
}
.centered-element {
    text-align: center;
}

.centered-element-h2 {
    text-align: center;
    position: relative;
    top: 0px;
    left: 0px;
}
.centered-element-h3 {
    text-align: center;
    position: relative;
    top: 0px;
    left: 60px;
}
</style>
"""

st.set_page_config(page_title="Hỏi và đáp", page_icon=":speech_balloon:")
openai.api_key = st.secrets["OPENAI_API_KEY"]

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = [
        AIMessage(content="Xin chào tôi là trợ lý thông minh. Bạn vui lòng đưa ra câu hỏi nhé?"),
    ]
st.markdown(html, unsafe_allow_html=True)
police_avatar_path = "static/police_vietnam.jpg"
human_avatar_path = "static/human_vietnam.jpg"
logo_path = "static/logo.png"
st.logo(logo_path)
# logo_path = "./app/static/logo.png"
# Add an image to the top left corner of the page
# st.markdown(f'<img src="{logo_path}" class="top-left-image" width="250" height="250">', unsafe_allow_html=True)
st.markdown('<h2 class="centered-element">HỎI ĐÁP CUỘC THI</h2>', unsafe_allow_html=True)
st.markdown(
    '<h3 class="centered-element">TÌM HIỂU PHÁP LUẬT VỀ CĂN CƯỚC, ĐỊNH DANH VÀ</h3>',
    unsafe_allow_html=True)
st.markdown(
    '<h3 class="centered-element">XÁC THỰC ĐIỆN TỬ CỦA VIỆT NAM</h3>',
    unsafe_allow_html=True)

for message in st.session_state.conversation_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI", avatar=police_avatar_path):
            st.markdown(message.content.replace("\n", "<br>"), unsafe_allow_html=True)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human", avatar=human_avatar_path):
            st.markdown(message.content)

user_query = st.chat_input("User: ")
if user_query is not None and user_query.strip() != "":
    st.session_state.conversation_history.append(HumanMessage(content=user_query))
    with st.chat_message("Human", avatar=human_avatar_path):
        st.markdown(user_query)

    with st.chat_message("AI", avatar=police_avatar_path):
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
