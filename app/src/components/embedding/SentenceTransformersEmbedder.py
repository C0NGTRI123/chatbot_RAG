from typing import List
from sentence_transformers import SentenceTransformer


class SentenceTransformersEmbedder:
    """Embeddings class to embed documents and queries with a SentenceTransformer model."""

    def __init__(
        self,
        model: str = "sentence-transformers/all-MiniLM-L6-v2"
    ):
        self.model = SentenceTransformer(model, trust_remote_code=True)

    def embed_embeddings(self, texts: List[str]):
        return self.model.encode(texts, batch_size=16, show_progress_bar=True, normalize_embeddings=True)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed documents."""
        return [self.model.encode(t, batch_size=16, show_progress_bar=True, normalize_embeddings=True).tolist() for t in
                texts]

    def embed_query(self, text: str) -> List[float]:
        """Embed query."""
        return self.model.encode(text, batch_size=16, show_progress_bar=True, normalize_embeddings=True).tolist()
