import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Placenix AI Chatbot", layout="wide")

st.title("🤖 AI Chatbot Assistant")
st.markdown("Get task prompts, learning advice, and placement preparation support.")

# Simulated chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", key="chat_input")

if user_input:
    # Add user input to history
    st.session_state.chat_history.append(("user", user_input))

    # Placeholder AI response
    if "resume" in user_input.lower():
        bot_response = "Sure! Let’s work on enhancing your resume using Semantic Role Labeling."
    elif "task" in user_input.lower():
        bot_response = "Here's a task for today: Practice 3 DP problems on Leetcode and summarize them."
    else:
        bot_response = "That sounds interesting! Let me get back to you with some guidance shortly."

    st.session_state.chat_history.append(("bot", bot_response))

# Display chat
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"🧑‍💻 **You:** {message}")
    else:
        st.markdown(f"🤖 **Placenix AI:** {message}")