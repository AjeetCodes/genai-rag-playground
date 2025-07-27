import os
from dotenv import load_dotenv
import requests
import streamlit as st
import json
load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey='+api_key)
news_results = requests.get(url=url)
data = news_results.json()

# data = json.loads(data)
print('news Dict', data)
# print(news_results.json())
st.set_page_config(layout="wide")
st.header("Today's Top News")
with st.spinner("Searching..."):
    if data['status'] == 'ok' and data['totalResults'] > 0:
        for article in data['articles']:
            with st.container(border=True):
                st.title(article.get('title', 'No Title'))
                st.text(article.get('author', 'Unknown Author'))
                st.subheader(article.get('description', 'No Description'))
                
                # Only show image if present
                if article.get('urlToImage'):
                    st.image(article['urlToImage'])
                
                st.text(article.get('publishedAt', 'Unknown Date'))
                
                # Only show content if present
                content = article.get('content')
                if content:
                    st.markdown(content)