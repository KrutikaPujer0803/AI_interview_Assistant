
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
    st.error('GROQ_API_KEY is missing. Add it to streamlit cloud --> App setting')
    st.stop()

role = st.selectbox("Select Job Role", [
    "Python Developer",
    "Java Developer",
    "Data Analyst",
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer"
])

if st.button("Generate Interview Questions"):
    prompt = "Generate 5 interview questions for the role of " + role

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are an expert technical Interviewer"},
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content
    st.write(output)
