import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# Page Config
st.set_page_config(page_title="💬 Gemini Chatbot", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #f9f9f9;
        }
        .chat-header {
            text-align: center;
            margin-bottom: 20px;
        }
        .chat-header h1 {
            color: #333;
        }
        .uploaded-file {
            font-size: 14px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    selected_tone = st.selectbox("Assistant Tone", ["Friendly", "Professional", "Funny", "Technical"])
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.experimental_rerun()

    uploaded_file = st.file_uploader("📎 Upload a text file (optional context)", type=["txt"])
    uploaded_content = ""
    if uploaded_file:
        uploaded_content = uploaded_file.read().decode("utf-8")
        st.markdown("<div class='uploaded-file'>✅ File uploaded</div>", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="chat-header">
    <h1>🤖 Gemini Chatbot</h1>
    <p>LangChain + Streamlit + Gemini AI</p>
</div>
""", unsafe_allow_html=True)

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").markdown(f"🧑‍💻 **You:** {msg.content}")
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").markdown(f"🤖 **Gemini:** {msg.content}")

# Chat input
if prompt := st.chat_input("Type your message..."):

    # Add user message
    st.chat_message("user").markdown(f"🧑‍💻 **You:** {prompt}")
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Build system prompt using tone and optional file
    system_prefix = f"You are a {selected_tone.lower()} assistant."
    if uploaded_content:
        system_prefix += f" Use this file context to help: {uploaded_content[:500]}"

    # Add system prompt only if first message
    if len(st.session_state.messages) == 1:
        st.session_state.messages.insert(0, HumanMessage(content=system_prefix))

    # LLM response
    with st.spinner("Gemini is thinking..."):
        response = llm.invoke(st.session_state.messages)

    st.chat_message("assistant").markdown(f"🤖 **Gemini:** {response.content}")
    st.session_state.messages.append(AIMessage(content=response.content))

# Footer
st.markdown("""
<hr>
<div style='text-align: center; font-size: 14px; color: gray;'>
Made with ❤️ using Streamlit + Gemini + LangChain
</div>
""", unsafe_allow_html=True)
