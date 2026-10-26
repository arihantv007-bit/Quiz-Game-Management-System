# Quiz Game Management System

A Python-based quiz application demonstrating Data Structures and Algorithms (DSA), CSV file handling, and Matplotlib data visualization.

## Features
- Student registration and ID-based lookup
- Category-wise quizzes (Python, DSA, Computer)
- Automatic score and percentage calculation
- Leaderboard using each student's best attempt
- CSV-based student, question, and quiz-result storage
- Dashboard with category attempts, score distribution, top scores, and date-wise activity

## DSA and Python Concepts
- Classes and objects
- Singly linked list
- Queue using `collections.deque`
- Binary search on sorted student IDs
- Bubble sort for leaderboard
- Lists, loops, functions, dictionaries, file handling, and exception handling

## Files
- `main.py` — main quiz application
- `dashboard.py` — Matplotlib analytics dashboard
- `students.csv` — sample student records
- `questions.csv` — quiz question bank
- `quiz_results.csv` — sample attempt records for testing charts
- `requirements.txt` — Python dependency

## Setup
Python 3.9 or later is recommended.

```bash
python -m pip install -r requirements.txt
python main.py
```

Register a student or use a sample ID from `students.csv`, such as `STU001`, to play a quiz. Choose menu option 5 to open the dashboard. The dashboard saves `dashboard.png`.

## CSV Data
The included student and result rows are sample data for demonstration. Replace them with your own test data before publishing if needed. The program creates missing CSV files automatically; it does not overwrite existing files.

## Author
Python and DSA academic project.
