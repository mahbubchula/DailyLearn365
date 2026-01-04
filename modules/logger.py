import pandas as pd
import os

def save_log(path, date, domain, topic, learning_type, depth, time_spent, insight):
    new_row = {
        "date": date,
        "domain": domain,
        "topic": topic,
        "learning_type": learning_type,
        "depth": depth,
        "time_spent_min": time_spent,
        "insight": insight
    }

    if os.path.exists(path):
        df = pd.read_csv(path)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])

    df.to_csv(path, index=False)

