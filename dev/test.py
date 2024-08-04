import streamlit as st
import json
import time


def text_streamer(text, delay=0.1):
    for i in range(0, len(text), 80):
        st.write(text[i:i + 80])
        time.sleep(delay)


with open("correct_answer.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    questions = [entry["question"] for entry in data]
    answers = [entry["answer"] for entry in data]

question = questions[0]
answer = answers[0]

# add stream text to the app
st.title("Question and Answer")
st.write(f"Question: {question}")


for chunk in text_streamer(answer.replace("\n", "<br>")):
    st.markdown(chunk, unsafe_allow_html=True)
