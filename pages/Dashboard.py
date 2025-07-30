import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Placenix Dashboard", layout="wide")

st.title("📊 Dashboard")
st.markdown("Welcome to your personalized placement readiness dashboard!")

# Sample metrics (replace with dynamic data later)
col1, col2, col3 = st.columns(3)
col1.metric("Overall Readiness", "72%", "+5%")
col2.metric("Coding Practice", "60%", "-3%")
col3.metric("Resume Score", "85%", "+10%")

st.markdown("### 📅 Weekly Progress")
st.line_chart(np.random.randn(10, 3), use_container_width=True)

st.markdown("### 🔍 Skill Gap Breakdown")
skill_data = {
    "Skill": ["Data Structures", "OOP", "DBMS", "OS", "Networking"],
    "Score": [60, 75, 50, 65, 70],
}
df = pd.DataFrame(skill_data)
st.bar_chart(df.set_index("Skill"))