import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(layout="wide")
api_key = os.getenv('GEMINI_API_KEY')
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
text = st.text_area("Enter your text or story", placeholder="Enter your text or story")

if st.button("submit") and text:
    query = """
        Summarize this text in 5-6 sentences -: {}
    """.format(text)
    # print(query)
    with st.spinner("Gemini is thinking..."):
        response = llm.invoke(query)
        try:
            if response:
                st.subheader("Response")
                with st.container(border=True):
                    st.markdown("""
                        {}
                    """.format(response.content))
        except Exception as e:
            st.warning(f"Error:{str(e)}")