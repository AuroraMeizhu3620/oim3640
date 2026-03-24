from __future__ import annotations

from tracking import summarize_counts
from utils import full_name


def build_student_report_rows(data: dict) -> list[dict]:
    counts = summarize_counts(data)
    settings = data["settings"]
    rows = []
    total_sessions = len(data["sessions"])
    for student in sorted(data["students"], key=full_name):
        student_counts = counts[student["id"]]
        attendance_total = student_counts["attendance_total"]
        attendance_present = student_counts["attendance_present"]
        participation_total = student_counts["participation_total"]

        attendance_pct = 0.0
        if attendance_total:
            attendance_pct = attendance_present / attendance_total

        max_participation = total_sessions or 1
        participation_pct = min(participation_total / max_participation, 1.0)

        weighted_score = (
            attendance_pct * settings["attendance_weight"]
            + participation_pct * settings["participation_weight"]
        )

        rows.append(
            {
                "student_id": student["id"],
                "name": full_name(student),
                "email": student.get("email", ""),
                "attendance_present": attendance_present,
                "attendance_total": attendance_total,
                "participation_total": participation_total,
                "attendance_pct": attendance_pct,
                "participation_pct": participation_pct,
                "weighted_score": weighted_score,
            }
        )
    return rows


def dashboard_summary(data: dict) -> dict:
    return {
        "student_count": len(data["students"]),
        "seat_count": len(data["seats"]),
        "session_count": len(data["sessions"]),
        "assigned_seat_count": len([seat for seat in data["assignments"].values() if seat]),
    }
