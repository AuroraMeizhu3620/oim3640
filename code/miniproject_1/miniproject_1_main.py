# Data storage setup
import json # for saving and loading data
from datetime import date # for current date
from pathlib import Path # for storing file path into variables
data_path = Path("data.json")

def load_data(): # if the file exists, load the file; if not, create new data structure 
    if data_path.exists():
        return json.loads(data_path.read_text(encoding="utf-8")) # reading numbers as text
    else:
        return {
            "students": [],        # sheet of students
            "seats": [],           # sheet of seat IDs
            "assignments": {},     # seat_id -> student_id
            "sessions": []         # sheet of session records
        }

def save_data(data):
    data_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    
def full_name(s):
    parts = [s["first"], s.get("middle","").strip(), s["last"]]
    return " ".join([p for p in parts if p])
