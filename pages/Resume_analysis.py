import streamlit as st
import time  # 👈 Add this line
from datetime import date

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("📄 Resume Analyzer")
st.markdown("Upload your resume to get an instant breakdown of your skills, gaps, and suggestions.")

# Upload Resume
uploaded_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])

# Simulate analysis (to be replaced with actual ML logic later)
if uploaded_file:
    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    with st.spinner("Analyzing resume..."):
        time.sleep(2)
    st.subheader("📌 Summary Insights")
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Detected Skills", value="Python, SQL, ML")
        st.metric(label="Matching Job Roles", value="Data Analyst, ML Engineer")
    
    with col2:
        st.metric(label="Experience Level", value="Intermediate")
        st.metric(label="Soft Skill Score", value="7.8 / 10")

    st.subheader("📈 Suggestions for Improvement")
    st.markdown("""
    - Add more project links with clear outcomes  
    - Highlight impact metrics in work experience  
    - Include keywords like 'Data Pipeline', 'API Integration'  
    - Consider contributing to open-source projects
    """)

    st.subheader("📅 Weekly Action Plan")
    st.success("🎯 This week: Add one new project to GitHub and update resume.")
else:
    st.warning("Please upload your resume to begin analysis.")