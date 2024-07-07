from sentence_transformers import SentenceTransformer, CrossEncoder
import faiss
from tqdm import tqdm
import os

sentence_embedding = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')


def faiss_search(query, k=15, index=None, metadatas=None, threshold=None):
    query_embedding = sentence_embedding.encode([query], normalize_embeddings=True)
    D, I = index.search(query_embedding, k)
    if threshold is None:
        results = [metadatas[i] for i in I[0]]
    else:
        results = [metadatas[i] for i, d in zip(I[0], D[0]) if d > threshold]

    return results


def load_faiss_index(save_path):
    return faiss.read_index(save_path)


def build_vector_database(embeddings, save_path):
    if not os.path.exists(save_path):
        d = embeddings.shape[1]
        index = faiss.IndexFlatIP(d)
        for i in tqdm(range(0, len(embeddings), 1000), desc="Build vector database: "):
            index.add(embeddings[i:i + 1000])
    faiss.write_index(index, save_path)
    return index


def rerank_context(query, context, k=3):
    cross_inp = [[query, context[i]] for i in range(len(context))]
    cross_scores = cross_encoder.predict(cross_inp)
    cross_scores = sorted(enumerate(cross_scores), key=lambda x: x[1], reverse=True)
    cross_scores = cross_scores[:k]
    results = [context[i] for i, _ in cross_scores]
    result = results[0]
    return result
