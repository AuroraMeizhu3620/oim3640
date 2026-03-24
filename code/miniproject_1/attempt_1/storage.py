from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

from models import make_layout, make_settings
from seating import build_seats

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "instance" / "data.json"


def default_data() -> dict:
    layout = make_layout()
    return {
        "students": [],
        "layout": layout,
        "seats": build_seats(layout["rows"], layout["cols"]),
        "assignments": {},
        "sessions": [],
        "settings": make_settings(),
    }


def ensure_data_file() -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_PATH.exists():
        DATA_PATH.write_text(json.dumps(default_data(), indent=2), encoding="utf-8")


def load_data() -> dict:
    ensure_data_file()
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    merged = deepcopy(default_data())
    merged.update(data)
    if not merged.get("seats"):
        layout = merged.get("layout", make_layout())
        merged["seats"] = build_seats(layout["rows"], layout["cols"])
    return merged


def save_data(data: dict) -> None:
    ensure_data_file()
    DATA_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
