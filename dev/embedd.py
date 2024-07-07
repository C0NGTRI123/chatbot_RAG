from typing import List


class SentenceTransformersEmbedder:
    """Embeddings class to embed documents and queries with a SentenceTransformer model."""

    def __init__(
        self,
        vectorizer: str
    ):
        super().__init__()
        self.vectorizer = vectorizer
        self.model = None
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(self.vectorizer)
        except Exception as e:
            pass

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed documents."""
        return [self.model.encode(t).tolist() for t in texts]

    def embed_query(self, text: str) -> List[float]:
        """Embed query."""
        return self.model.encode(text).tolist()


# a = SentenceTransformersEmbedder("sentence-transformers/all-MiniLM-L6-v2")
