# Student Analysis

A small Python project for loading and summarizing student marks from CSV data.

## Usage

```python
from student_analysis import load_students, summarize_students

students = load_students("data/students.csv")
summary = summarize_students(students)
print(summary)
```

## Run tests

```bash
python -m pytest -q
```
