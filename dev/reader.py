import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("../correct_answer.json", "r") as file:
    data = json.load(file)
    questions = [entry["question"] for entry in data]
    answers = [entry["answer"] for entry in data]
    query = "Vì sao phải đổi tên Luật Căn cước công dân thành Luật Căn cuoc cong dan"

question_embeddings = model.encode(questions)
query_embedding = model.encode([query])

# Compute similarities
similarities = cosine_similarity(query_embedding, question_embeddings)
print(similarities)

# Find the index of the most similar question
most_similar_idx = np.argmax(similarities)

# Retrieve the most similar question and its corresponding answer
most_similar_question = questions[most_similar_idx]
most_similar_answer = answers[most_similar_idx]

print(f"Most similar question: {most_similar_question}")
print(f"Answer: {most_similar_answer}")



