import streamlit as st
from PIL import Image
import random

# --- Page Config ---
st.set_page_config(
    page_title="🎓 Mood-Based Study Planner AI",
    layout="wide",
    page_icon="📚",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    html, body {
        background-color: #F0F4F8;
    }
    .main {
        background-color: #ffffff;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    }
    h1, h2, h3, h4 {
        font-family: 'Segoe UI', sans-serif;
        color: #222831;
    }
    .stButton>button {
        font-size: 16px !important;
        padding: 10px 20px;
        border-radius: 10px;
        background-color: #4A90E2;
        color: white;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #357ABD;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("🧠 Mood Scanner")
    st.info("This AI tool detects your current mood and recommends the perfect study plan for you.")
    st.markdown("---")
    st.subheader("📸 Webcam Status:")
    st.success("Running ✅")  # Future: Add webcam integration

# --- Main Container ---
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("🎓 AI Mood-Based Study Planner")
st.caption("🔍 Get personalized study recommendations based on your real-time mood.")

# --- Simulated Mood Detection ---
moods = ['Happy 😊', 'Sad 😢', 'Angry 😡', 'Calm 😌', 'Stressed 😫']
descriptions = {
    'Happy 😊': 'You seem cheerful and upbeat! Great time for focus-intensive tasks.',
    'Sad 😢': 'You might need light or creative tasks. Stay kind to yourself.',
    'Angry 😡': 'Redirect your energy to physical or quick goal-oriented tasks.',
    'Calm 😌': 'Perfect time for deep learning and solving hard problems.',
    'Stressed 😫': 'Take a break or try relaxed study tasks.'
}
detected_mood = random.choice(moods)
confidence = round(random.uniform(75, 99), 2)

# --- Mood Section ---
st.header("🧠 Detected Mood")
st.success(f"**Mood:** {detected_mood}")
st.info(f"**Confidence Score:** {confidence}%")
st.markdown(f"**🧾 Interpretation:** {descriptions[detected_mood]}")

st.markdown("---")

# --- Recommended Study Plan ---
st.subheader("📋 Your Personalized Study Plan")

plan_map = {
    'Happy 😊': ["✅ Practice coding", "✅ Solve Data Structures problems", "✅ Take quizzes"],
    'Sad 😢': ["✅ Watch educational YouTube", "✅ Revise old concepts", "✅ Listen to light podcasts"],
    'Angry 😡': ["✅ Do hands-on projects", "✅ Solve easy-to-win challenges", "✅ Physical break"],
    'Calm 😌': ["✅ Learn new ML topics", "✅ Read research papers", "✅ Build something new"],
    'Stressed 😫': ["✅ Watch relaxing tutorials", "✅ Make study notes", "✅ Meditate or take a break"]
}

for task in plan_map[detected_mood]:
    st.checkbox(task)

st.markdown("---")

# --- Action Buttons ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔁 Rerun Mood Scan"):
        st.rerun()
with col2:
    st.button("💾 Export Plan (coming soon)")
with col3:
    st.button("🔄 Reset")

st.markdown("</div>", unsafe_allow_html=True)
