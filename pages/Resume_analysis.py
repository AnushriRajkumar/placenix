import streamlit as st
import base64

st.set_page_config(page_title="Placenix Resume Analyzer", layout="wide")

st.title("📄 Resume Analyzer")
st.markdown("Upload your resume and receive AI-driven feedback to boost your placement chances.")

# Upload Section
uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")
    file_details = {
        "filename": uploaded_file.name,
        "filetype": uploaded_file.type,
        "filesize": uploaded_file.size,
    }
    st.json(file_details)

    st.markdown("---")
    st.markdown("### 📊 Analysis Overview")

    # Placeholder data
    st.write("**Skill Match:** 72%")
    st.write("**Detected Keywords:** Python, SQL, Data Analysis, Machine Learning")
    st.write("**Suggestions:**")
    st.markdown("- Add more project-based experience.")
    st.markdown("- Include specific tools (e.g., Scikit-learn, Pandas).")
    st.markdown("- Mention internships with measurable impact.")

    st.markdown("---")
    st.markdown("### 📈 Resume Score")
    st.progress(0.72)

else:
    st.info("Please upload a resume to see analysis.")