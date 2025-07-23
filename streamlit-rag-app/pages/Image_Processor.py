import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

st.set_page_config(layout="wide")
st.title("Image Processor Chat App")
uploaded_file = st.file_uploader("Upload An Image", type=['png', 'jpg', 'jpeg'])
user_query = st.text_input("Write your query related to an uploaded image", placeholder="Write your query related to an image")
language_prompts = {
    "Hindi" : "इसका उत्तर हिंदी में दें:",
    "Engilist" : "Answer this in English:",
    "French": "Répondez à ceci en français :",
    "Spanish": "Responde esto en español:"
}

language = st.selectbox("Choose response language", ["English", "Hindi", "French", "Spanish"])
if st.button("Submit", type='primary') and uploaded_file and user_query and language:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    with st.spinner("LLm model is thinking..."):
        response = model.generate_content([
            f"{language_prompts[language]} {user_query}",
            image
        ])
        with st.container(border=True):
            st.markdown(response.text)