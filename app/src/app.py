import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from app.src.services.pdf_service import PDFService


# Input fields for the user to specify parameters
file_path = st.text_input('Enter the path to the PDF file:', '')
query = st.text_input('Enter your query:', '')
mode = st.selectbox('Select mode:', options=['character', 'recursive', 'semantic'])
search_rank = st.number_input('Enter search rank:', min_value=1, value=25)
rerank_rank = st.number_input('Enter rerank rank:', min_value=1, value=3)
save_path = st.text_input('Enter the path to save the FAISS index:', '')

# Button to trigger processing
if st.button('Process PDF'):
    if file_path and query and save_path:
        # Initialize PDFService with user inputs
        pdf_service = PDFService(file_path=file_path, query=query, mode=mode, search_rank=search_rank,
                                 rerank_rank=rerank_rank, save_path=save_path)

        # Process the PDF and get results
        results = pdf_service.extract()

        # Display the results
        st.write('Results:')
        st.write(results)
    else:
        st.error('Please fill in all the fields.')