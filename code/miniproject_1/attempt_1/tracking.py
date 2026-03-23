from __future__ import annotations

from collections import defaultdict


def student_session_history(data: dict, student_id: str) -> list[dict]:
    history = []
    for session in data["sessions"]:
        history.append(
            {
                "date": session["date"],
                "attendance": session["attendance"].get(student_id, "Absent"),
                "participation": int(session["participation"].get(student_id, 0)),
                "notes": session.get("notes", ""),
            }
        )
    return history


def summarize_counts(data: dict) -> dict[str, dict]:
    counts = defaultdict(
        lambda: {
            "attendance_present": 0,
            "attendance_total": 0,
            "participation_total": 0,
        }
    )
    for session in data["sessions"]:
        for student_id, status in session["attendance"].items():
            counts[student_id]["attendance_total"] += 1
            if status == "Present":
                counts[student_id]["attendance_present"] += 1
        for student_id, count in session["participation"].items():
            counts[student_id]["participation_total"] += int(count)
    return counts
