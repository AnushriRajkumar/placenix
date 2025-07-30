import streamlit as st
import time

st.set_page_config(page_title="Placenix Mock Interview", layout="wide")

st.title("🎤 Mock Interview")
st.markdown("Practice technical + HR interviews with AI-based evaluation of your answers.")

# Tabs for different interview types
interview_type = st.radio("Select Interview Type", ["Technical", "HR", "Custom"], horizontal=True)

# Question display area
st.markdown("### 🧠 Interview Question")
st.write("Describe a project you've worked on and the challenges you faced.")

# Text input for answer
user_answer = st.text_area("Your Answer", height=150)

# Button to submit
if st.button("Submit Answer"):
    with st.spinner("Analyzing your response..."):
        time.sleep(2)  # Placeholder for backend AI analysis

    # Fake evaluation (we’ll later use Wave2Vec, MediaPipe, DistilBERT, etc.)
    st.markdown("### ✅ AI Feedback")
    st.write("**Clarity:** 80%")
    st.write("**Confidence:** 70%")
    st.write("**Content Quality:** 75%")
    st.success("Try to be more specific about tools used and outcomes achieved.")

# Optional: webcam/audio button placeholders
with st.expander("🎥 Advanced Mock Interview (Coming Soon)"):
    st.info("This feature will analyze body language and speech emotions using OpenFace, MediaPipe, and Wave2Vec.")