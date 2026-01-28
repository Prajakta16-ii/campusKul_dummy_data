import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# ---------------- POSTS ----------------
num_posts = 800
posts = pd.DataFrame({
    "post_id": range(1, num_posts + 1),
    "user_id": np.random.randint(1, 1001, num_posts),
    "role": np.random.choice(["student", "faculty", "mentor"], num_posts, p=[0.7, 0.2, 0.1]),
    "college_id": np.random.choice([101, 102, 103, 104], num_posts),
    "content_type": np.random.choice(["text", "image", "video"], num_posts),
    "created_at": [
        datetime.now() - timedelta(days=random.randint(0, 90))
        for _ in range(num_posts)
    ]
})

posts.to_csv("posts.csv", index=False)

# ---------------- COMMENTS ----------------
num_comments = 2000
comments = pd.DataFrame({
    "comment_id": range(1, num_comments + 1),
    "post_id": np.random.choice(posts["post_id"], num_comments),
    "user_id": np.random.randint(1, 1001, num_comments),
    "role": np.random.choice(["student", "faculty", "mentor"], num_comments, p=[0.7, 0.2, 0.1]),
    "college_id": np.random.choice([101, 102, 103, 104], num_comments),
    "created_at": [
        datetime.now() - timedelta(days=random.randint(0, 90))
        for _ in range(num_comments)
    ]
})

comments.to_csv("comments.csv", index=False)

# ---------------- JOBS ----------------
num_jobs = 200
jobs = pd.DataFrame({
    "job_id": range(1, num_jobs + 1),
    "company": np.random.choice(["Google", "Amazon", "Infosys", "TCS", "Microsoft"], num_jobs),
    "job_type": np.random.choice(["internship", "full-time"], num_jobs),
    "college_id": np.random.choice([101, 102, 103, 104], num_jobs),
    "posted_at": [
        datetime.now() - timedelta(days=random.randint(0, 90))
        for _ in range(num_jobs)
    ]
})

jobs.to_csv("jobs.csv", index=False)

# ---------------- APPLICATIONS ----------------
num_apps = 1500
applications = pd.DataFrame({
    "application_id": range(1, num_apps + 1),
    "job_id": np.random.choice(jobs["job_id"], num_apps),
    "user_id": np.random.randint(1, 1001, num_apps),
    "role": ["student"] * num_apps,
    "college_id": np.random.choice([101, 102, 103, 104], num_apps),
    "applied_at": [
        datetime.now() - timedelta(days=random.randint(0, 90))
        for _ in range(num_apps)
    ]
})

applications.to_csv("applications.csv", index=False)

print("Dummy CSV files created successfully")
