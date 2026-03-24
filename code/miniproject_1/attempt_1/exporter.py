from __future__ import annotations

from io import BytesIO

from openpyxl import Workbook

from scoring import build_student_report_rows
from tracking import student_session_history


def export_excel(data: dict) -> BytesIO:
    workbook = Workbook()
    summary_sheet = workbook.active
    summary_sheet.title = "Student Summary"
    summary_sheet.append(
        [
            "Student ID",
            "Name",
            "Email",
            "Attendance Present",
            "Attendance Total",
            "Participation Total",
            "Attendance %",
            "Participation %",
            "Weighted Score",
        ]
    )

    report_rows = build_student_report_rows(data)
    for row in report_rows:
        summary_sheet.append(
            [
                row["student_id"],
                row["name"],
                row["email"],
                row["attendance_present"],
                row["attendance_total"],
                row["participation_total"],
                round(row["attendance_pct"], 2),
                round(row["participation_pct"], 2),
                round(row["weighted_score"], 2),
            ]
        )

    history_sheet = workbook.create_sheet("Session History")
    history_sheet.append(["Student ID", "Name", "Date", "Attendance", "Participation", "Notes"])
    students_by_id = {student["id"]: student for student in data["students"]}
    for row in report_rows:
        student_id = row["student_id"]
        student = students_by_id[student_id]
        for history in student_session_history(data, student_id):
            history_sheet.append(
                [
                    student_id,
                    row["name"],
                    history["date"],
                    history["attendance"],
                    history["participation"],
                    history["notes"],
                ]
            )

    output = BytesIO()
    workbook.save(output)
    output.seek(0)
    return output
