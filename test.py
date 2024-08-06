import streamlit as st

st.set_page_config(page_title="Hỏi và đáp", page_icon=":speech_balloon:")

# Add a custom logo to the page base css
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

# Apply the CSS
st.markdown(html, unsafe_allow_html=True)

logo_path = "./app/static/logo.png"
# Add an image to the top left corner of the page
st.markdown(f'<img src="{logo_path}" class="top-left-image" width="300" height="300">', unsafe_allow_html=True)
st.markdown('<h2 class="centered-element">HỎI ĐÁP CUỘC THI</h2>', unsafe_allow_html=True)
st.markdown(
    '<h3 class="centered-element">TÌM HIỂU PHÁP LUẬT VỀ CĂN CƯỚC, ĐỊNH DANH VÀ</h3>',
    unsafe_allow_html=True)
st.markdown(
    '<h3 class="centered-element">XÁC THỰC ĐIỆN TỬ CỦA VIỆT NAM</h3>',
    unsafe_allow_html=True)