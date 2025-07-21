import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
from langchain.vectorstores import Chroma

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

st.set_page_config(layout="wide")
st.title("📺 YouTube Chat App")
st.write("Paste a YouTube link and chat with the video transcript.")
# Load Chroma vectorstore
vectorstore = Chroma(
    persist_directory="./chroma_store",  # Same dir used during saving
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
)
# Create Retriever
retriever = vectorstore.as_retriever()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
# RAG Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True  # Optional: show source context
)
query = st.text_input("Type your question here:", placeholder="Write your query")
if st.button("Submit") and query:
    result = qa_chain(query)
    
    st.subheader("🔍 Answer:")
    st.write(result["result"])
    
    # Optional: Show sources
    with st.expander("📄 Source Chunks Used"):
        for doc in result["source_documents"]:
            st.markdown(doc.page_content)