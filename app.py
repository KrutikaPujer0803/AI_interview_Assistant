import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Interview Assistant",
    layout="centered"
)

st.title("AI Interview Assistant")

st.caption(
    "Practice interviews with AI-generated questions "
    "and constructive feedback."
)

st.caption("Launched by Krutika")
st.write("Department of AI&DS")

st.title('AI Interview Assistant')
st.caption('Practice Interviews with AI-generated questions')
try:
    client = Groq(api_key=st.secrets['GROQ_API_KEY'])
    st.write("API connect successful")
except (KeyError, FileNotFoundError):
    st.error('GROQ_API_KEY is missing.Add it to streamlit cloud -->App setting')
    st.stop()

