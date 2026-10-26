import csv
import os
import random
import subprocess
import sys
from datetime import datetime
from collections import deque

BASE = os.path.dirname(os.path.abspath(__file__))
STUDENTS = os.path.join(BASE, "students.csv")
QUESTIONS = os.path.join(BASE, "questions.csv")
RESULTS = os.path.join(BASE, "quiz_results.csv")

STUDENT_FIELDS = ["student_id", "name", "branch"]
QUESTION_FIELDS = [
    "question_id", "category", "question",
    "option_a", "option_b", "option_c", "option_d",
    "correct_option"
]
RESULT_FIELDS = [
    "result_id", "student_id", "name", "category",
    "score", "total_questions", "percentage", "date", "time"
]

SAMPLE_QUESTIONS = [
    ["Q001", "Python", "Which keyword defines a function?", "func", "def", "function", "define", "B"],
    ["Q002", "Python", "Which data type stores unique values?", "List", "Tuple", "Set", "String", "C"],
    ["Q003", "Python", "Which symbol starts a comment in Python?", "//", "#", "/*", "--", "B"],
    ["Q004", "DSA", "Which data structure follows FIFO?", "Stack", "Queue", "Tree", "Graph", "B"],
    ["Q005", "DSA", "Which data structure follows LIFO?", "Queue", "Array", "Stack", "Linked List", "C"],
    ["Q006", "DSA", "Binary search requires which condition?", "Random data", "Sorted data", "Duplicate data", "Empty data", "B"],
    ["Q007", "Python", "Which keyword is used for a loop?", "repeat", "loop", "for", "iterate", "C"],
    ["Q008", "Computer", "What is the brain of a computer?", "RAM", "CPU", "SSD", "Monitor", "B"],
    ["Q009", "DSA", "Which structure connects nodes using links?", "Linked List", "Integer", "String", "Float", "A"],
    ["Q010", "Computer", "Which one is an input device?", "Monitor", "Speaker", "Keyboard", "Projector", "C"],
    ["Q011", "Python", "Which method adds an item to a list?", "append()", "insertEnd()", "pushBack()", "attach()", "A"],
    ["Q012", "DSA", "Which algorithm repeatedly swaps adjacent elements?", "Binary Search", "Bubble Sort", "DFS", "Merge Search", "B"],
    ["Q013", "Computer", "What does RAM primarily provide?", "Permanent storage", "Temporary working memory", "Printing", "Internet access", "B"],
    ["Q014", "Python", "Which file mode is used to append data?", "r", "w", "a", "x", "C"],
    ["Q015", "DSA", "Which structure is commonly used for BFS?", "Queue", "Stack only", "Heap only", "Variable", "A"]
]


def initialize_files():
    files = [
        (STUDENTS, STUDENT_FIELDS, []),
        (QUESTIONS, QUESTION_FIELDS, SAMPLE_QUESTIONS),
        (RESULTS, RESULT_FIELDS, [])
    ]
    for path, fields, sample in files:
        if not os.path.exists(path):
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(fields)
                writer.writerows(sample)


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def next_id(prefix, rows, field):
    numbers = []
    for row in rows:
        value = row[field]
        if value.startswith(prefix) and value[len(prefix):].isdigit():
            numbers.append(int(value[len(prefix):]))
    return f"{prefix}{max(numbers, default=0) + 1:03d}"


class Student:
    """Represents a registered quiz participant."""
    def __init__(self, student_id, name, branch):
        self.id = student_id
        self.name = name
        self.branch = branch


class StudentNode:
    def __init__(self, student):
        self.student = student
        self.next = None


class StudentLinkedList:
    """Singly linked list used to store and display student objects."""
    def __init__(self):
        self.head = None

    def insert(self, student):
        node = StudentNode(student)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def display(self):
        current = self.head
        while current:
            s = current.student
            print(f"{s.id:<10} {s.name:<22} {s.branch}")
            current = current.next


def binary_search(rows, student_id):
    """Binary search requires rows sorted by student_id."""
    low, high = 0, len(rows) - 1
    target = student_id.upper()
    while low <= high:
        mid = (low + high) // 2
        current = rows[mid]["student_id"].upper()
        if current == target:
            return rows[mid]
        if current < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def register_student():
    rows = read_csv(STUDENTS)
    name = input("Enter your name: ").strip()
    branch = input("Enter your branch: ").strip().upper()
    if not name or not branch:
        print("Name and branch cannot be empty.")
        return

    student_id = next_id("STU", rows, "student_id")
    rows.append({
        "student_id": student_id,
        "name": name,
        "branch": branch
    })
    write_csv(STUDENTS, rows, STUDENT_FIELDS)
    print("\nRegistration successful!")
    print("Your Student ID:", student_id)
    print("Use this ID for future quizzes.")


def show_students():
    rows = sorted(read_csv(STUDENTS),
                  key=lambda row: row["student_id"].upper())
    linked_list = StudentLinkedList()
    for row in rows:
        linked_list.insert(
            Student(row["student_id"], row["name"], row["branch"])
        )
    print("\nREGISTERED STUDENTS")
    print(f"{'ID':<10} {'Name':<22} Branch")
    linked_list.display()


def find_student(student_id):
    rows = sorted(read_csv(STUDENTS),
                  key=lambda row: row["student_id"].upper())
    return binary_search(rows, student_id)


def play_quiz():
    student_id = input("Enter your registered Student ID: ").strip()
    student = find_student(student_id)
    if not student:
        print("Student not found. Please register first.")
        return

    questions = read_csv(QUESTIONS)
    if not questions:
        print("No questions available.")
        return

    categories = sorted({q["category"] for q in questions})
    print("\nQUIZ CATEGORIES")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    print(f"{len(categories) + 1}. All categories")

    choice = input("Choose category: ").strip()
    if not choice.isdigit():
        print("Invalid choice.")
        return

    number = int(choice)
    if number == len(categories) + 1:
        selected = questions[:]
        category = "Mixed"
    elif 1 <= number <= len(categories):
        category = categories[number - 1]
        selected = [q for q in questions if q["category"] == category]
    else:
        print("Invalid choice.")
        return

    random.shuffle(selected)
    question_queue = deque(selected[:5])
    if not question_queue:
        print("No questions available in this category.")
        return

    total = len(question_queue)
    score = 0
    print(f"\nWelcome, {student['name']}!")
    print(f"Category: {category} | Questions: {total}")

    question_number = 1
    while question_queue:
        q = question_queue.popleft()
        print(f"\nQ{question_number}. {q['question']}")
        print("A.", q["option_a"])
        print("B.", q["option_b"])
        print("C.", q["option_c"])
        print("D.", q["option_d"])
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        while answer not in ("A", "B", "C", "D"):
            answer = input("Enter A, B, C or D: ").strip().upper()

        if answer == q["correct_option"].strip().upper():
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect. Correct option:", q["correct_option"])
        question_number += 1

    percentage = round(score / total * 100, 2)
    now = datetime.now()
    results = read_csv(RESULTS)
    results.append({
        "result_id": next_id("RES", results, "result_id"),
        "student_id": student["student_id"],
        "name": student["name"],
        "category": category,
        "score": score,
        "total_questions": total,
        "percentage": percentage,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S")
    })
    write_csv(RESULTS, results, RESULT_FIELDS)

    print("\n===== QUIZ RESULT =====")
    print("Student:", student["name"])
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage}%")
    print("Result saved in quiz_results.csv")


def show_leaderboard():
    results = read_csv(RESULTS)
    if not results:
        print("No quiz attempts recorded yet.")
        return

    best = {}
    for row in results:
        sid = row["student_id"]
        percentage = float(row["percentage"])
        if sid not in best or percentage > float(best[sid]["percentage"]):
            best[sid] = row

    leaderboard = list(best.values())
    # Bubble sort: highest percentage first
    for i in range(len(leaderboard)):
        for j in range(len(leaderboard) - i - 1):
            if float(leaderboard[j]["percentage"]) < float(
                    leaderboard[j + 1]["percentage"]):
                leaderboard[j], leaderboard[j + 1] = (
                    leaderboard[j + 1], leaderboard[j]
                )

    print("\n===== LEADERBOARD: BEST ATTEMPT =====")
    for rank, row in enumerate(leaderboard, 1):
        print(f"{rank}. {row['name']} | {row['percentage']}% "
              f"| {row['score']}/{row['total_questions']} "
              f"| {row['category']}")


def open_dashboard():
    path = os.path.join(BASE, "dashboard.py")
    if not os.path.exists(path):
        print("dashboard.py not found.")
        return
    subprocess.Popen([sys.executable, path], cwd=BASE)


def main():
    initialize_files()
    while True:
        print("\n" + "=" * 42)
        print("      QUIZ GAME MANAGEMENT SYSTEM")
        print("=" * 42)
        print("1. Register Student")
        print("2. Play Quiz")
        print("3. View Registered Students")
        print("4. View Leaderboard")
        print("5. Open Visualization Dashboard")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                register_student()
            elif choice == "2":
                play_quiz()
            elif choice == "3":
                show_students()
            elif choice == "4":
                show_leaderboard()
            elif choice == "5":
                open_dashboard()
            elif choice == "6":
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice. Try again.")
        except (OSError, csv.Error, KeyError, ValueError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
