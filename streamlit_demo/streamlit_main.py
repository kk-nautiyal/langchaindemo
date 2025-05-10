from langchain_openai import ChatOpenAI
import streamlit as st

st.title("Ask Anything")

with st.sidebar:
    OPENAI_API_KEY= st.text_input("Enter your OpenAI Key")
    
if not OPENAI_API_KEY:
    st.info("Enter your OpenAI Key")
    st.stop()    

llm = ChatOpenAI(model = "gpt-4o", api_key=OPENAI_API_KEY)

question = st.text_input("Enter your questions: ")

if question:
    response = llm.invoke(question)
    st.write(response)

