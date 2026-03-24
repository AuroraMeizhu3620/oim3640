from __future__ import annotations


def seat_label(row: int, col: int) -> str:
    return f"R{row + 1}C{col + 1}"


def build_seats(rows: int, cols: int) -> list[dict]:
    seats = []
    for row in range(rows):
        for col in range(cols):
            seat_id = seat_label(row, col)
            seats.append(
                {
                    "id": seat_id,
                    "label": seat_id,
                    "row": row + 1,
                    "col": col + 1,
                }
            )
    return seats


def normalize_assignments(seats: list[dict], assignments: dict) -> dict:
    valid_seat_ids = {seat["id"] for seat in seats}
    normalized = {}
    for seat_id, student_id in assignments.items():
        if seat_id in valid_seat_ids and student_id:
            normalized[seat_id] = student_id
    return normalized
