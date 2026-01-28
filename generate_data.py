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
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

num_events = 5000

event_names = [
    "Tech Fest 2025",
    "Student Leadership Workshop",
    "AI & Data Science Seminar",
    "Campus Placement Drive",
    "Entrepreneurship Bootcamp",
    "Hackathon 2025"
]

event_types = [
    "Workshop",
    "Academic Conference",
    "Seminar",
    "Hackathon"
]

locations = ["Mumbai", "Pune", "Delhi", "Bangalore"]
user_names = ["pritish123", "saurabh123", "admin01", "faculty01"]

events = pd.DataFrame({
    "event_id": range(1, num_events + 1),

    # who viewed / applied / interacted
    "user_id": np.random.choice(users["user_id"], num_events),

    # event details
    "event_name": np.random.choice(event_names, num_events),
    "event_type": np.random.choice(event_types, num_events),
    "location": np.random.choice(locations, num_events),
    "created_by": np.random.choice(user_names, num_events),

    # dates
    "start_date": [
        datetime.now() + timedelta(days=random.randint(1, 60))
        for _ in range(num_events)
    ],
    "end_date": [
        datetime.now() + timedelta(days=random.randint(61, 90))
        for _ in range(num_events)
    ],

    # event tracking timestamp (when user interacted)
    "interaction_timestamp": [
        datetime.now() - timedelta(days=random.randint(0, 90))
        for _ in range(num_events)
    ]
})

events.to_csv("events.csv", index=False)

print("Events CSV created successfully!")
