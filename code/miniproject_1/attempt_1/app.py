from __future__ import annotations

from flask import Flask, flash, redirect, render_template, request, send_file, url_for

from exporter import export_excel
from models import make_session, make_student
from scoring import build_student_report_rows, dashboard_summary
from seating import build_seats, normalize_assignments
from storage import load_data, save_data
from utils import today_iso

app = Flask(__name__)
app.config["SECRET_KEY"] = "classroom-superassistant-dev"


@app.route("/")
def index():
    data = load_data()
    return render_template("dashboard.html", summary=dashboard_summary(data))


@app.route("/students", methods=["GET", "POST"])
def students():
    data = load_data()
    if request.method == "POST":
        first = request.form.get("first", "").strip()
        last = request.form.get("last", "").strip()
        middle = request.form.get("middle", "").strip()
        email = request.form.get("email", "").strip()
        if not first or not last:
            flash("First and last name are required.", "error")
        else:
            data["students"].append(make_student(first=first, last=last, middle=middle, email=email))
            save_data(data)
            flash("Student added.", "success")
            return redirect(url_for("students"))
    students_sorted = sorted(data["students"], key=lambda student: (student["last"], student["first"]))
    return render_template("students.html", students=students_sorted)


@app.route("/students/delete/<student_id>", methods=["POST"])
def delete_student(student_id: str):
    data = load_data()
    data["students"] = [student for student in data["students"] if student["id"] != student_id]
    data["assignments"] = {
        seat_id: assigned_student_id
        for seat_id, assigned_student_id in data["assignments"].items()
        if assigned_student_id != student_id
    }
    for session in data["sessions"]:
        session["attendance"].pop(student_id, None)
        session["participation"].pop(student_id, None)
    save_data(data)
    flash("Student deleted.", "success")
    return redirect(url_for("students"))


@app.route("/seating", methods=["GET", "POST"])
def seating():
    data = load_data()
    if request.method == "POST":
        action = request.form.get("action")
        if action == "generate":
            rows = max(1, int(request.form.get("rows", 4)))
            cols = max(1, int(request.form.get("cols", 5)))
            data["layout"] = {"rows": rows, "cols": cols}
            data["seats"] = build_seats(rows, cols)
            data["assignments"] = normalize_assignments(data["seats"], data["assignments"])
            save_data(data)
            flash("Seating layout updated.", "success")
            return redirect(url_for("seating"))
        if action == "assign":
            assignments = {}
            for seat in data["seats"]:
                student_id = request.form.get(f"seat_{seat['id']}", "").strip()
                if student_id:
                    assignments[seat["id"]] = student_id
            data["assignments"] = normalize_assignments(data["seats"], assignments)
            save_data(data)
            flash("Seat assignments saved.", "success")
            return redirect(url_for("seating"))
    students_sorted = sorted(data["students"], key=lambda student: (student["last"], student["first"]))
    students_by_id = {student["id"]: student for student in data["students"]}
    return render_template(
        "seating.html",
        layout=data["layout"],
        seats=data["seats"],
        assignments=data["assignments"],
        students=students_sorted,
        students_by_id=students_by_id,
    )


@app.route("/sessions/new", methods=["GET", "POST"])
def new_session():
    data = load_data()
    students_sorted = sorted(data["students"], key=lambda student: (student["last"], student["first"]))
    if request.method == "POST":
        session_date = request.form.get("session_date", today_iso())
        notes = request.form.get("notes", "")
        attendance = {}
        participation = {}
        for student in students_sorted:
            student_id = student["id"]
            attendance[student_id] = request.form.get(f"attendance_{student_id}", "Absent")
            participation[student_id] = int(request.form.get(f"participation_{student_id}", 0) or 0)
        data["sessions"].append(make_session(session_date, attendance, participation, notes))
        save_data(data)
        flash("Session recorded.", "success")
        return redirect(url_for("reports"))
    return render_template("session_form.html", students=students_sorted, today=today_iso())


@app.route("/reports", methods=["GET", "POST"])
def reports():
    data = load_data()
    if request.method == "POST":
        data["settings"]["attendance_weight"] = max(0, min(100, int(request.form.get("attendance_weight", 40))))
        data["settings"]["participation_weight"] = max(0, min(100, int(request.form.get("participation_weight", 60))))
        save_data(data)
        flash("Scoring settings updated.", "success")
        return redirect(url_for("reports"))
    rows = build_student_report_rows(data)
    return render_template("reports.html", rows=rows, settings=data["settings"], sessions=data["sessions"])


@app.route("/export")
def export():
    data = load_data()
    workbook = export_excel(data)
    return send_file(
        workbook,
        as_attachment=True,
        download_name="classroom_report.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


if __name__ == "__main__":
    app.run(debug=True)
