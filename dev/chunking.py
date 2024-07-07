from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

embed_model = FastEmbedEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
loader = PyPDFLoader("1810.04805.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False
)

naive_chunks = text_splitter.split_documents(documents)
for chunk in naive_chunks:
    print(chunk.page_content + "\n")

# rag_template = """Use the following context to answer the user's query. If you cannot answer, please respond with 'I don't know'.
#
#             User's Query:
#             {question}
#
#             Context:
#             {context}
# """
#
# rag_prompt = ChatPromptTemplate.from_template(rag_template)
# naive_chunk_vectorstore = Chroma.from_documents(naive_chunks, embedding=embed_model)
# naive_chunk_retriever = naive_chunk_vectorstore.as_retriever(search_kwargs={"k": 5})
# # print(naive_chunk_retriever.invoke("Describe the Self-RAG"))
#
#
# naive_rag_chain = (
#     {"context": naive_chunk_retriever, "question": RunnablePassthrough()}
#     | rag_prompt
#     | chat_model
#     | StrOutputParser()
# )
#
# print(naive_rag_chain.invoke("Describe the SELF-RAG?"))