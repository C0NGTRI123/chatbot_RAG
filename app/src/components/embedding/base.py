from abc import ABC, abstractmethod


class Embedding(ABC):
    @abstractmethod
    def embed_documents(self, texts):
        pass

    @abstractmethod
    def embed_query(self, text):
        pass
