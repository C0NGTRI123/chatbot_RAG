import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from app.src.services.pdf_service import PDFService
import openai

# def get_base64_image(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode()
#
#
# background_image = get_base64_image("img/tg_image_1984667092.png")
# overlay_image = get_base64_image("img/LOGO2.png")

# html_content = f"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <style>
#         .image-container {{
#             position: relative;
#             display: inline-block;
#         }}
#         .image-container img {{
#             display: block;
#             width: 50%;
#             height: 50%;
#         }}
#         .overlay {{
#             position: absolute;
#             top: 0;
#             left: 0;
#             max-width: 231px;
#             margin-top: 10px;
#         }}
#     </style>
# </head>
# <body>
#     <div class="image-container">
#         <img src="data:image/png;base64,{background_image}" alt="Background Image">
#         <img src="data:image/png;base64,{overlay_image}" class="overlay" alt="Overlay Image">
#     </div>
# </body>
# </html>
# """

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

st.set_page_config(page_title="Hỏi và đáp", page_icon=":speech_balloon:")
openai.api_key = st.secrets["OPENAI_API_KEY"]

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = [
        AIMessage(content="Xin chào tôi là trợ lý thông minh. Bạn vui lòng đưa ra câu hỏi nhé?"),
    ]

police_avatar_path = "img/police_vietnam.jpg"
human_avatar_path = "img/human_vietnam.jpg"

st.image("img/LOGO2.png", width=150)
st.markdown('<h2 class="centered-element">HỎI ĐÁP CUỘC THI</h2>', unsafe_allow_html=True)
st.markdown(
    '<h3 class="centered-element">TÌM HIỂU PHÁP LUẬT VỀ CĂN CƯỚC, ĐỊNH DANH VÀ XÁC THỰC ĐIỆN TỬ CỦA VIỆT NAM</h3>',
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
