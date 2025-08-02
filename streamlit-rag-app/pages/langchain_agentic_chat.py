import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from tools.get_weather import get_weather
from langchain.tools import tool
from tools.summarizer import summarize
load_dotenv()
st.set_page_config(layout="wide")
api_key = os.getenv("GEMINI_API_KEY")

st.title("Multi-Agent Gemini Assistant")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)


weather_tools = [
    Tool(
        name="GetWeather",
        func=get_weather,
        description="Use this tool to get the weather of a city. Input should be the city name."
    )
]

summary_tools = [
    Tool(
        name="GetSummary",
        func=summarize,
        description="Use this tool to summarize the text. Input should be the input text."
    )
]

def initAgent(toolsName :str):
    agent = initialize_agent(
        tools=toolsName,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    return agent


def route(query:str) -> str:
    query = query.lower()
    if 'weather' in query or 'temperature' in query:
        agent = initAgent(weather_tools)
        return agent.run(query)
    elif 'summarize' in query or 'summarry' in query:
        agent = initAgent(summary_tools)
        return agent.run(query)
    else:
        return "Please include 'weather' or 'summarize' in your query"
# query = st.text_input("Enter Your Query", placeholder="Enter Your Query")
query = st.text_area("🧠 Ask a question", placeholder="Try: What's the weather in Delhi?\nOr: Summarize this article: ...")
if st.button("Ask", type="primary") and query :
    with st.spinner("Thinking.."):
        # res = agent.run(query)
        res = route(query)
        # print('res', res)
        with st.container(border=True):
            st.success("Response Generated!")
            st.markdown(res)
