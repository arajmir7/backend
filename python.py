#!/usr/bin/env python3
"""
DAILY PROOF GENERATOR (WINDOWS SAFE)
Run with:
    py proof.py
"""

import os
import datetime

# ================= AUTO =================

TODAY = datetime.date.today()
DATE = TODAY.strftime("%d-%m-%Y")
TIME_COMPLETED = datetime.datetime.now().strftime("%H:%M")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "daily-proofs")

START_FILE = os.path.join(BASE_DIR, ".start_date")

if not os.path.exists(START_FILE):
    with open(START_FILE, "w", encoding="utf-8") as f:
        f.write(DATE)

with open(START_FILE, encoding="utf-8") as f:
    start_date = datetime.datetime.strptime(f.read(), "%d-%m-%Y").date()

DAY_NUMBER = (TODAY - start_date).days + 1

# ================= DAILY INPUT =================

LEETCODE_EASY = [
    {"id": "66", "name": "Plus One", "runtime": "45ms"},
]

HACKERRANK = [
    {"name": "Arrays Left Rotation", "score": "10/10"},
]

PROJECT_NAME = "Practice & DSA"
PROJECT_FEATURES = ["Python basics", "Arrays"]
TOTAL_HOURS = 5.0
ROW_STATUS = "✅ ON TRACK"

# ================= LOGIC =================

def generate_proof():
    proof = f"""🔥 **DAY {DAY_NUMBER} PROOF – {DATE}**

## WORK DONE
- LeetCode Easy: {len(LEETCODE_EASY)}
- HackerRank: {len(HACKERRANK)}

## PROJECT
- {PROJECT_NAME}
- Features: {", ".join(PROJECT_FEATURES)}

## TRACKING
- Hours: {TOTAL_HOURS}
- Status: {ROW_STATUS}

## TIME COMPLETED
- {TIME_COMPLETED}
"""

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"day-{DAY_NUMBER}-proof-{DATE.replace('-', '')}.md"
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(proof)

    print("✅ Proof generated successfully")
    print(f"📄 {path}")

if __name__ == "__main__":
    generate_proof()
