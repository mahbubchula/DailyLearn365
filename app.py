import streamlit as st
import pandas as pd
from datetime import date
import os

from modules.logger import save_log
from modules.analytics import compute_streak, summary_stats
from modules.visualization import plot_time_spent, plot_domain_distribution

DATA_PATH = "data/daily_logs.csv"

st.set_page_config(
    page_title="DailyLearn365",
    page_icon="📘",
    layout="wide"
)

st.title("📘 DailyLearn365")
st.subheader("A 365-Day Structured Learning Tracker")

# ---------- Load Data ----------
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
else:
    df = pd.DataFrame()

# ---------- Sidebar ----------
st.sidebar.header("📊 Learning Overview")

if not df.empty:
    streak = compute_streak(df)
    total_days = df["date"].nunique()
    total_time = df["time_spent_min"].sum()

    st.sidebar.metric("🔥 Current Streak (days)", streak)
    st.sidebar.metric("📅 Total Logged Days", total_days)
    st.sidebar.metric("⏱️ Total Time (minutes)", total_time)
else:
    st.sidebar.info("No learning data yet.")

# ---------- Daily Input Form ----------
st.markdown("## ✍️ Log Today’s Learning")

with st.form("daily_learning_form"):
    learning_date = st.date_input("Date", value=date.today())

    domain = st.selectbox(
        "Learning Domain",
        [
            "Transportation Engineering",
            "Machine Learning",
            "AI / LLM",
            "Programming",
            "Research Writing",
            "Tool Development",
            "Other"
        ]
    )

    topic = st.text_input("Topic / Concept Learned")

    learning_type = st.selectbox(
        "Learning Type",
        ["Reading", "Coding", "Experiment", "Lecture", "Reflection"]
    )

    depth = st.selectbox(
        "Depth Level",
        ["Surface", "Applied", "Theoretical"]
    )

    time_spent = st.number_input(
        "Time Spent (minutes)",
        min_value=0,
        step=10
    )

    insight = st.text_area(
        "Key Insight / Reflection",
        height=120
    )

    submit = st.form_submit_button("💾 Save Learning Entry")

if submit:
    save_log(
        DATA_PATH,
        learning_date,
        domain,
        topic,
        learning_type,
        depth,
        time_spent,
        insight
    )
    st.success("✅ Learning entry saved successfully!")

# ---------- Analytics Section ----------
st.markdown("---")
st.markdown("## 📈 Learning Analytics")

if not df.empty:
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(plot_time_spent(df), use_container_width=True)

    with col2:
        st.plotly_chart(plot_domain_distribution(df), use_container_width=True)

    st.markdown("### 📋 Summary Statistics")
    st.dataframe(summary_stats(df), use_container_width=True)

else:
    st.info("Analytics will appear once you start logging learning.")

