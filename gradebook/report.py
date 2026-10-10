"""Plain-text report for the terminal."""

from .core import letter_grade, rank_students


def format_report(records):
    ranking = rank_students(records)
    lines = [f"{'#':>2}  {'Name':<12} {'Score':>5}  Grade"]
    for position, (score, name) in enumerate(ranking, start=1):
        lines.append(f"{position:>2}  {name:<12} {score:>5.1f}  {letter_grade(score)}")
    if ranking:
        mean = sum(score for score, _ in ranking) / len(ranking)
        lines.append(f"Class average: {mean:.1f}")
    return "\n".join(lines)
