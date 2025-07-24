import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from get_weather import get_weather

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)


tools = [
    Tool(
        name="GetWeather",
        func=get_weather,
        description="Use this tool to get the weather of a city. Input should be the city name."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

query = st.text_input("Enter Your Query", placeholder="Enter Your Query")
if st.button("Ask Question", type="primary") and query :
    with st.spinner("Thinking.."):
        res = agent.run(query)
        # print('res', res)
        with st.container(border=True):
            st.success("Response Generated!")
            st.markdown(res)
