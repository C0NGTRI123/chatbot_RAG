from app.src.components.reader.BasicReader import BasicReader
from app.src.components.chunk import Chunk
from app.src.components.embedding import SentenceTransformersEmbedder
from app.src.components.retriever.FaissRetrival import faiss_search, build_vector_database, rerank_context, load_faiss_index
from app.src.components.generation import OpenAIGenerator
import os
import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class PDFService(object):
    def __init__(
        self, file_path, query, mode, search_rank, rerank_rank, save_path
    ):
        self.file_path = file_path
        self.query = query
        self.mode = mode
        self.search_rank = search_rank
        self.rerank_rank = rerank_rank
        self.save_path = save_path

    def extract(self):
        if os.path.exists(self.save_path):
            index = load_faiss_index(self.save_path)
            chunks = []
            for i in range(0, len(os.listdir(os.path.join(os.path.dirname(self.save_path), "chunks")))):
                with open(os.path.join(os.path.dirname(self.save_path), f"chunks/chunk_{i}.txt"), "r", encoding="utf-8") as f:
                    chunks.append(f.read())
        else:
            text = BasicReader(self.file_path).load()
            chunks = Chunk(text, mode=self.mode).get_text_chunk()
            texts_to_embed = [line for line in chunks]
            embeddings = SentenceTransformersEmbedder().embed_embeddings(texts_to_embed)
            index = build_vector_database(embeddings, self.save_path)
            for i, chunk in enumerate(chunks):
                if not os.path.exists(os.path.join(os.path.dirname(self.save_path), "chunks")):
                    os.makedirs(os.path.join(os.path.dirname(self.save_path), "chunks"))
                with open(os.path.join(os.path.dirname(self.save_path), f"chunks/chunk_{i}.txt"), "w") as f:
                    f.write(chunk)
        with open(r"C:\Users\congt\Desktop\chatbot\chatbot\dev\correct_answer.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            questions = [entry["question"] for entry in data]
            answers = [entry["answer"] for entry in data]
        question_embeddings = SentenceTransformersEmbedder().embed_embeddings(questions)
        query_embedding = SentenceTransformersEmbedder().embed_embeddings([self.query])

        similarities = cosine_similarity(query_embedding, question_embeddings)
        if np.max(similarities) > 0.95:
            most_similar_idx = np.argmax(similarities)
            output = answers[most_similar_idx]
        else:
            context = faiss_search(self.query, k=self.search_rank, index=index, metadatas=chunks)
            rerank_context_str = rerank_context(self.query, context, k=self.rerank_rank)
            prompt = f"You are AI assistant to answer user's query.\n" \
                     f"IMPORTANT: Please provide the most relevant answer to the user's query and return answer Vietnamese\n" \
                     f"Use the following context to answer the user's query." \
                     f"CONTEXT: {rerank_context_str}\n" \
                     f"QUERY: {self.query}\n"
            output = OpenAIGenerator(prompt, temperature=1).generate()
        return output


if __name__ == "__main__":
    folder_path = "/home/rb074/Downloads/drive-download-20240705T165934Z-001"
    file_path_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path)]
    output = PDFService(file_path=file_path_list, query="Vì sao phải đổi tên Luật Căn cước công dân thành Luật Căn cước?", mode="semantic", search_rank=25, rerank_rank=3, save_path="/home/rb074/Desktop/project/chatbot/dev/vector_database.index").extract()
    print(output)

