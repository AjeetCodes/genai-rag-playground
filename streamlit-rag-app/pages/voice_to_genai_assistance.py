# app.py
import streamlit as st
# from voice_input import recognize_voice
# from voice_output import speak_text
# from langchain.chat_models import ChatGoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import speech_recognition as sr
from dotenv import load_dotenv

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

st.title("🗣️ Talk to GenAI")
st.set_page_config(layout="wide")
def speak_text(text):
    tts = gTTS(text=text, lang="en")
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio = AudioSegment.from_file(fp.name, format="mp3")
        play(audio)
        
def recognize_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        return query
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand the audio."
    
if st.button("🎤 Speak"):
    user_input = recognize_voice()
    st.write(f"**You said:** {user_input}")

    with st.spinner("Thinking..."):
        response = llm.invoke(user_input)
        st.success("AI says:")
        st.markdown(response.content)
        speak_text(response.content)
