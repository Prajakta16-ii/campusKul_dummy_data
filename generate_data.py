import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ---------------- USERS ----------------
num_users = 1000

users = pd.DataFrame({
    "user_id": range(1, num_users + 1),
    "role": np.random.choice(
        ["student", "faculty", "mentor", "admin"],
        num_users,
        p=[0.7, 0.15, 0.1, 0.05]
    ),
    "college_id": np.random.choice([101, 102, 103, 104], num_users),
    "created_at": [
        datetime.now() - timedelta(days=random.randint(0, 90))
        for _ in range(num_users)
    ]
})

users.to_csv("users.csv", index=False)

# ---------------- EVENTS ----------------
num_events = 5000

events = pd.DataFrame({
    "event_id": range(1, num_events + 1),
    "user_id": np.random.choice(users["user_id"], num_events),
    "event_name": np.random.choice(
        ["signup", "profile_complete", "post", "comment", "job_view", "job_apply","connect_people"],
        num_events
    ),
    "timestamp": [
        datetime.now() - timedelta(days=random.randint(0, 90))
        for _ in range(num_events)
    ]
})

events.to_csv("events.csv", index=False)

print("CSV files created successfully!")
