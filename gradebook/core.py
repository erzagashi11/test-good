"""Load grades from CSV and compute per-student results."""

import csv
from dataclasses import dataclass

WEIGHTS = {"homework": 0.3, "midterm": 0.3, "final": 0.4}
LETTER_BOUNDS = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]


@dataclass(frozen=True)
class StudentRecord:
    name: str
    homework: float
    midterm: float
    final: float


def load_records(path):
    """Read a CSV with the columns name,homework,midterm,final."""
    records = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            records.append(
                StudentRecord(
                    name=row["name"].strip(),
                    homework=_parse_score(row["homework"]),
                    midterm=_parse_score(row["midterm"]),
                    final=_parse_score(row["final"]),
                )
            )
    return records


def _parse_score(raw):
    value = float(raw)
    if not 0 <= value <= 100:
        raise ValueError(f"score out of range 0..100: {raw}")
    return value


def weighted_final_score(record):
    """Combine the three parts using WEIGHTS, rounded to one decimal."""
    total = (
        record.homework * WEIGHTS["homework"]
        + record.midterm * WEIGHTS["midterm"]
        + record.final * WEIGHTS["final"]
    )
    return round(total, 1)


def letter_grade(score):
    for bound, letter in LETTER_BOUNDS:
        if score >= bound:
            return letter
    return "F"


def rank_students(records):
    """Highest score first; equal scores keep alphabetical order."""
    scored = [(weighted_final_score(record), record.name) for record in records]
    return sorted(scored, key=lambda item: (-item[0], item[1]))
