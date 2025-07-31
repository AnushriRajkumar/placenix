import streamlit as st
import datetime
import random

st.set_page_config(page_title="Placenix | Dashboard", layout="wide")

st.title("📊 Placenix Dashboard")
st.image("https://api.dicebear.com/8.x/bottts/svg?seed=PlacenixUser", width=100, caption="Your Avatar 🤖")
st.markdown("Welcome back! Here's your progress overview:")

# --- Skill Badges ---
st.subheader("🎖️ Your Skill Badges")
badge_cols = st.columns(4)

badges = {
    "Communication": "🗣️",
    "Coding": "💻",
    "Problem Solving": "🧠",
    "Teamwork": "🤝",
}

for i, (skill, emoji) in enumerate(badges.items()):
    with badge_cols[i]:
        st.markdown(f"### {emoji} {skill}")
        st.success("Unlocked ✅")
# --- Daily Streak ---
st.subheader("🔥 Your Daily Streak")

# For now, let’s simulate a 5-day streak (we'll replace it with real logic later)
current_streak = 5
streak_emoji = "🔥" * current_streak
st.metric("Active Days", f"{current_streak} days")
st.markdown(f"**{streak_emoji}**")

st.divider()

# --- Readiness Score ---
st.subheader("📈 Placement Readiness")

readiness = random.randint(60, 85)  # Replace with real value later
st.progress(readiness / 100)
st.info(f"You are {readiness}% ready. Keep it up! 💪")

st.divider()

# --- Task Suggestion ---
st.subheader("📌 Quick Task Suggestion")

tasks = [
    "✅ Complete a mock interview",
    "✍️ Update your resume",
    "🧠 Solve 3 LeetCode questions",
    "🤖 Ask Placenix chatbot for a 1-hour productivity plan",
]

suggestion = random.choice(tasks)
st.markdown(f"**Today’s Task:** {suggestion}")
st.divider()
st.markdown("## ✅ Daily Task Checklist")

# Simulated task list
tasks = {
    "Completed Mock Interview": False,
    "Analyzed Resume": False,
    "Used AI Chatbot": False,
    "Checked Dashboard": False
}

# Store completed task count
completed_tasks = 0

# Display tasks with checkboxes
for task in tasks:
    if st.checkbox(task, key=task):
        completed_tasks += 1
# Simulated XP values
xp_per_task = 10
total_xp = completed_tasks * xp_per_task
level = total_xp // 40 + 1  # Every 40 XP = level up
xp_progress = total_xp % 40

# XP progress bar
st.write(f"**Level {level}**")
st.progress(xp_progress / 40)

# Optional motivational quote
if total_xp > 0:
    st.caption("“Greatness is a lot of small things done well every day.” 🌟")