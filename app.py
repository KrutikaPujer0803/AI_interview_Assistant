
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

st.divider()

try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

    st.success("API connection successful")

except (KeyError, FileNotFoundError):
    st.error(
        "GROQ_API_KEY is missing. "
        "Add it to Streamlit Cloud settings."
    )
    st.stop()

role = st.selectbox(
    "Select Job Role",
    [
        "Python Developer",
        "Java Developer",
        "Data Analyst",
        "Frontend Developer",
        "Backend Developer",
        "Full Stack Developer"
    ]
)

if st.button("Generate Interview Questions"):

    prompt = f"""
    Generate 5 technical interview questions
    for the job role of {role}.

    Include:
    1. Beginner-level questions
    2. Intermediate-level questions
    3. Questions related to practical skills

    Number the questions clearly.
    """

    try:
        with st.spinner("Generating interview questions..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert technical interviewer. "
                            "Generate clear and useful interview questions."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            output = response.choices[0].message.content

        st.subheader("Interview Questions")
        st.write(output)

    except Exception as e:
        st.error("Unable to generate questions.")
        st.write(e)
