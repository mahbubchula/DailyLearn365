import pandas as pd
from datetime import datetime, timedelta

def compute_streak(df):
    dates = pd.to_datetime(df["date"]).dt.date.unique()
    dates = sorted(dates, reverse=True)

    streak = 0
    today = dates[0]

    for i, d in enumerate(dates):
        if i == 0 or d == today - timedelta(days=i):
            streak += 1
        else:
            break

    return streak

def summary_stats(df):
    return pd.DataFrame({
        "Metric": [
            "Total Days Logged",
            "Total Time (minutes)",
            "Average Time per Day",
            "Unique Domains"
        ],
        "Value": [
            df["date"].nunique(),
            df["time_spent_min"].sum(),
            round(df["time_spent_min"].mean(), 2),
            df["domain"].nunique()
        ]
    })

