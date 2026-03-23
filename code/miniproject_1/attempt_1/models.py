from __future__ import annotations

from utils import generate_id


def make_student(first: str, last: str, middle: str = "", email: str = "") -> dict:
    return {
        "id": generate_id("stu"),
        "first": first.strip(),
        "middle": middle.strip(),
        "last": last.strip(),
        "email": email.strip(),
    }


def make_layout(rows: int = 4, cols: int = 5) -> dict:
    return {
        "rows": rows,
        "cols": cols,
    }


def make_settings() -> dict:
    return {
        "attendance_weight": 40,
        "participation_weight": 60,
    }


def make_session(session_date: str, attendance: dict, participation: dict, notes: str = "") -> dict:
    return {
        "id": generate_id("ses"),
        "date": session_date,
        "attendance": attendance,
        "participation": participation,
        "notes": notes.strip(),
    }
