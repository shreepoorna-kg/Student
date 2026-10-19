import csv
from pathlib import Path


def load_students(csv_path):
    """Load student records from a CSV file."""
    students = []
    with Path(csv_path).open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = {
                "name": row["name"],
                "math": int(row["math"]),
                "science": int(row["science"]),
                "english": int(row["english"]),
            }
            students.append(student)
    return students


def summarize_students(students):
    """Return summary statistics for a list of student records."""
    if not students:
        return {
            "student_count": 0,
            "average_math": 0.0,
            "average_science": 0.0,
            "average_english": 0.0,
            "top_student": None,
        }

    math_scores = [student["math"] for student in students]
    science_scores = [student["science"] for student in students]
    english_scores = [student["english"] for student in students]

    averages = {
        "student_count": len(students),
        "average_math": round(sum(math_scores) / len(math_scores), 2),
        "average_science": round(sum(science_scores) / len(science_scores), 2),
        "average_english": round(sum(english_scores) / len(english_scores), 2),
    }

    top_student = max(students, key=lambda student: (
        student["math"] + student["science"] + student["english"]
    ))
    averages["top_student"] = top_student["name"]

    return averages
