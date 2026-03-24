from __future__ import annotations

from datetime import date
from uuid import uuid4


def generate_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:8]}"


def today_iso() -> str:
    return date.today().isoformat()


def full_name(student: dict) -> str:
    parts = [
        student.get("first", "").strip(),
        student.get("middle", "").strip(),
        student.get("last", "").strip(),
    ]
    return " ".join(part for part in parts if part)
