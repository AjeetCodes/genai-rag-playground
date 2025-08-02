def summarize(text:str) -> str :
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    return llm.invoke(f"Summarize this one in one sentence :- \n text: {text}")