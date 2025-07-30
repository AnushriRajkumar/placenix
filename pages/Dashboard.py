import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="Placenix Dashboard", layout="wide")
st.title("📊 Dashboard")
st.markdown("Welcome to your Placement Readiness Dashboard!")

# ----------------------
# Simulate Readiness Forecast Chart
# ----------------------
st.subheader("📈 Readiness Forecast (Time Series)")

# Simulated time series data
dates = pd.date_range(start=datetime.date.today(), periods=10)
readiness_scores = np.linspace(40, 85, num=10) + np.random.normal(0, 3, 10)

df = pd.DataFrame({
    "Date": dates,
    "Readiness Score": readiness_scores
})

st.line_chart(df.set_index("Date"))

# ----------------------
# Burnout Risk Meter
# ----------------------
st.subheader("🔥 Burnout Risk Prediction")

burnout_score = np.random.randint(10, 90)  # simulated

color = "🟢 Low"
if burnout_score > 70:
    color = "🔴 High"
elif burnout_score > 40:
    color = "🟠 Medium"

st.metric(label="Burnout Risk Score", value=f"{burnout_score}%", delta=None, help="Predicted using behavioral and physiological patterns")
st.markdown(f"Current Burnout Level: **{color}**")

# ----------------------
# Daily Task Checklist
# ----------------------
st.subheader("✅ Today's AI-Suggested Tasks")

tasks = {
    "Complete a mock interview": False,
    "Update your resume projects": True,
    "Revise 5 aptitude questions": False,
    "Practice DSA topic": True,
    "Reflect on 1 interview question": False
}

completed = 0
for task, status in tasks.items():
    checked = st.checkbox(task, value=status)
    if checked:
        completed += 1

st.success(f"🎉 You’ve completed {completed} / {len(tasks)} tasks today!")

if completed == len(tasks):
    st.balloons()
    st.markdown("🏅 **You’ve earned a daily reward badge!**")

# ----------------------
# Resume Status
# ----------------------
st.subheader("📝 Resume Strength")

resume_score = np.random.randint(50, 95)  # placeholder
resume_feedback = "Strong" if resume_score > 75 else "Needs More Projects"

st.info(f"Resume Score: **{resume_score}/100**")
st.markdown(f"🔍 Feedback: **{resume_feedback}**")

# ----------------------
# Last Mock Interview Feedback
# ----------------------
st.subheader("🎤 Mock Interview Summary")

mock_score = np.random.randint(40, 95)
st.warning(f"🧠 Your last interview score was **{mock_score}/100**")

if mock_score > 80:
    st.success("💡 Excellent! You're interview-ready.")
elif mock_score > 60:
    st.info("🙂 You're getting there. Keep practicing.")
else:
    st.error("😕 Let's work on those weak spots!")