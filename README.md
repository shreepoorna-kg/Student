# Student Analysis

Student Analysis is a simple Python project designed to read student performance data from a CSV file and generate meaningful summary statistics. It is useful for learning data handling, Python functions, and small-scale analytics in a clean, beginner-friendly project structure.

## Project Overview

This project focuses on a small dataset of student marks across three subjects: Math, Science, and English. The main goal is to:

- load student records from a CSV file
- calculate subject averages
- find the overall top-performing student
- keep the logic simple and easy to understand

It is ideal for classroom exercises, mini projects, and learning how to work with structured data in Python.

## Features

- Reads student data from a CSV file
- Converts numeric score values to integers
- Computes average marks for each subject
- Identifies the student with the highest total score
- Includes automated tests to validate the behavior

## Folder Structure

```text
student-analysis/
├── data/
│   └── students.csv
├── tests/
│   └── test_student_analysis.py
├── student_analysis.py
├── requirements.txt
├── README.md
├── .gitignore
└── .pytest_cache/
```

## Installation

1. Open a terminal in the project folder.
2. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

3. Activate the virtual environment:

- Windows:

```bash
.venv\Scripts\activate
```

- macOS/Linux:

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

```python
from student_analysis import load_students, summarize_students

students = load_students("data/students.csv")
summary = summarize_students(students)
print(summary)
```

Example output:

```python
{
    'student_count': 5,
    'average_math': 79.0,
    'average_science': 81.2,
    'average_english': 80.2,
    'top_student': 'Diana'
}
```

## How It Works

The program loads the CSV using Python's built-in `csv` module. Each row is interpreted as a student record containing:

- name
- math score
- science score
- english score

The summary function then calculates the average of each subject and ranks students by their total across all three subjects.

## Running Tests

To run the automated test suite:

```bash
python -m pytest -q
```

The tests verify that:

- CSV records are loaded correctly
- summary statistics match expected values
- the top student is identified correctly

## Why This Project Is Useful

This project introduces several important programming concepts:

- file input and output
- handling structured data
- basic statistics and aggregation
- modular code design
- automated testing with pytest

## Future Improvements

Some possible enhancements include:

- adding grade categories like Pass/Fail
- generating a final student report
- plotting subject performance using charts
- supporting larger datasets from Excel or JSON files

## License

This project is provided for educational purposes and can be freely modified and extended.

