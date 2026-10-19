import csv
from pathlib import Path

from student_analysis import load_students, summarize_students


def test_load_students_reads_csv(tmp_path):
    csv_path = tmp_path / "students.csv"
    csv_path.write_text(
        "name,math,science,english\n"
        "Alice,88,92,85\n"
        "Bob,70,78,80\n",
        encoding="utf-8",
    )

    students = load_students(csv_path)

    assert len(students) == 2
    assert students[0]["name"] == "Alice"
    assert students[0]["math"] == 88


def test_summarize_students_returns_expected_metrics():
    students = [
        {"name": "Alice", "math": 88, "science": 92, "english": 85},
        {"name": "Bob", "math": 70, "science": 78, "english": 80},
        {"name": "Charlie", "math": 60, "science": 65, "english": 72},
    ]

    summary = summarize_students(students)

    assert summary["student_count"] == 3
    assert summary["average_math"] == 72.67
    assert summary["average_science"] == 78.33
    assert summary["average_english"] == 79.0
    assert summary["top_student"] == "Alice"
