# Data storage setup
import json # for saving and loading data
from datetime import date # for current date
from pathlib import Path # for storing file path into variables
data_path = Path("data.json")

def load_data():
    if data_path.exists():
        return json.loads(DATA_PATH.read_text(encoding="utf-8"))
    return {
        "students": [],
        "seats": [],
        "assignments": {},   # seat_id -> student_id
        "sessions": []       # list of session dicts
    }