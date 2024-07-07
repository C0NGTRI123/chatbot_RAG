from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from app.src.components.embedding import SentenceTransformersEmbedder


class Chunk:
    def __init__(
        self,
        text: str = "",
        mode: str = "character"
    ):
        self.text = text
        self.mode = mode

    def get_text_chunk(self):
        if self.mode == "character":
            text_splitter = CharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
                is_separator_regex=False
            )

        elif self.mode == "recursive":
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
                is_separator_regex=False
            )

        elif self.mode == "semantic":
            embeddings = SentenceTransformersEmbedder("sentence-transformers/all-MiniLM-L6-v2")
            text_splitter = SemanticChunker(embeddings)
        chunks = text_splitter.split_text(self.text)
        return chunks
