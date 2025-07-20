import os
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import Chroma
# from langchain.retrievers import VectorStoreRetriever
from langchain.chains import RetrievalQA

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')


#UI part using streamlit
st.title("Fully Expanded Streamlit YouTube Chat App")
# st.header("YouTube Chat APP")
youtube_url = st.text_input("Enter YouTube URL")

# st.sidebar.title("Gen AI Playground")
st.set_page_config(page_title="GenAI RAG Playground", layout="wide")
# st.sidebar.markdown("Navigate between learning modules.")
def get_yt_video_id(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        return parse_qs(parsed_url.query)['v'][0]
    elif parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    else:
        raise ValueError("YouTube Video URL is not valid")
    
def generate_transcript(yt_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(yt_id, languages=["en", "hi"])
        fullTxt = "".join([line['text'] for line in transcript])
        return fullTxt
    except Exception as e:
        return f"Error fetching transcript -: {str(e)}"
    
if youtube_url:
    yt_id = get_yt_video_id(youtube_url)
    generated_txt = generate_transcript(yt_id)
    if generated_txt:
        with st.container(border=True):
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500)
            chunk = text_splitter.split_text(generated_txt)
            embiddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            vectore_store = Chroma.from_texts(
                texts=chunk,
                embedding=embiddings,
                persist_directory='./chroma_store'
            )
            res = vectore_store.persist()
            st.success("Text from YouTube Link Generated Successfully..")
            # st.subheader(f'Generated text')
            st.markdown(""" 
                <div style="margin-bottom : 15px; height: 400px; overflow-y: auto; padding: 10px; border: 1px solid #ccc; background-color: #f9f9f9;">
                    <pre style="white-space: pre-wrap;">
                        {}
                    </pre>
                </div>
            """.format(generated_txt), unsafe_allow_html=True)
            # Load Chroma vectorstore
            
