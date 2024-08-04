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

# Add custom CSS to set the background color
colors_css = """
<style>
.main {
  background-color: linear-gradient(to right, green 33.33%, white 33.33%);;
}
.white-font {
    color: white;
}
</style>
"""


st.set_page_config(page_title="Hỏi và đáp", page_icon=":speech_balloon:")
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Apply the CSS
st.markdown(center_elements_css, unsafe_allow_html=True)
st.markdown(left_elements_css, unsafe_allow_html=True)
st.markdown(right_elements_css, unsafe_allow_html=True)
st.markdown(colors_css, unsafe_allow_html=True)

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = [
        AIMessage(content="Xin chào tôi là trợ lý thông minh. Tôi có thể giúp gì cho bạn?"),
    ]

police_avatar_path = "assets/police_vietnam.png"
human_avatar_path = "assets/human_vietnam.jpg"
logo_path = "assets/logo.png"

# Display the logo with the custom CSS class
st.image(logo_path, width=100)


st.markdown('<h2 class="centered-element">HỎI ĐÁP CUỘC THI</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="left-element">TÌM HIỂU PHÁP LUẬT VỀ CĂN CƯỚC, ĐỊNH DANH VÀ XÁC THỰC ĐIỆN TỬ CỦA VIỆT NAM</h2>',
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