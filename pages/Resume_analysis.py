import streamlit as st
import time  # 👈 Add this line
from datetime import date

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("📄 Resume Analyzer")
st.markdown("Upload your resume to get an instant breakdown of your skills, gaps, and suggestions.")

# Upload Resume
uploaded_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
import pdfplumber

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")

    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Check for key sections
    with st.expander("🔍 Resume Insights"):
        required_sections = ["education", "skills", "experience", "projects", "certifications"]
        found = []
        missing = []

        for section in required_sections:
            if section.lower() in resume_text.lower():
                found.append(section)
            else:
                missing.append(section)

        st.markdown("### ✅ Found Sections")
        st.write(found)

        st.markdown("### ⚠️ Missing Sections")
        st.write(missing)

        if len(missing) == 0:
            st.success("Great! Your resume has all essential sections.")
        else:
            st.warning("Consider adding the missing sections for better completeness.")

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