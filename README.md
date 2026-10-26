# 🎮 Quiz Game Management System

### Test Your Knowledge. Track Your Progress. Visualize Your Performance.

A Python-based Quiz Game Management System built using **Object-Oriented Programming, Data Structures & Algorithms (DSA), CSV file handling, and Matplotlib**. Students can register, attempt topic-based quizzes, track their scores, and view leaderboard rankings, while the dashboard transforms quiz results into meaningful visualizations.

---

## 🚀 Project Highlights

- 🧑‍🎓 **Student Registration** — Register once and use your Student ID to play quizzes.
- 🧠 **Interactive Quiz Gameplay** — Answer multiple-choice questions from different categories.
- 📚 **Multiple Categories** — Practice Python, DSA, and Computer Fundamentals.
- 🏆 **Leaderboard System** — Compare performance and view top scores.
- 📊 **Data Visualization** — Generate charts to analyze quiz attempts, score distribution, top performers, and activity over time.
- 💾 **CSV-Based Storage** — Store student details, questions, and quiz results without requiring a database server.
- ⚡ **DSA Implementation** — Demonstrates linked lists, queues, searching, and sorting.
- 🔄 **Persistent Records** — Keep student and quiz records between program runs.

---

## 🖥️ Project Preview

The project runs through a menu-driven Python interface and generates a visual dashboard from quiz results.

**Dashboard visualizations include:**
- Category-wise quiz attempts
- Score distribution
- Top students by best score
- Date-wise quiz activity

> The dashboard is saved as `dashboard.png` when the visualization script runs successfully and valid result records are available.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| OOP | Classes, objects, constructors, and methods |
| CSV | Data storage and file handling |
| Data Structures | Linked lists and queues |
| Algorithms | Binary search and bubble sort |
| Matplotlib | Graphs and data visualization |
| Git & GitHub | Version control and project hosting |

---

## 🧩 DSA Concepts Used

| Concept | Implementation | Purpose |
|---|---|---|
| Classes & Objects | `Student` | Organizes student information |
| Singly Linked List | `StudentLinkedList` and `StudentNode` | Manages student records |
| Queue | `deque` | Organizes questions for a quiz session |
| Binary Search | Student ID lookup | Searches for a registered student |
| Bubble Sort | Leaderboard sorting | Ranks quiz results |
| Lists & Loops | Quiz and question processing | Manages gameplay and repeated operations |

These concepts demonstrate how fundamental DSA techniques can be applied to a practical Python application.

---

## 📂 Project Structure

```text
Quiz-Game-Management-System/
│
├── main.py             # Main application and quiz gameplay
├── dashboard.py        # Data visualization and chart generation
├── students.csv        # Registered student records
├── questions.csv       # Quiz questions and answer keys
├── quiz_results.csv    # Quiz performance records
├── dashboard.png       # Generated visualization dashboard
├── requirements.txt    # Required Python packages
├── README.md           # Project documentation
└── .gitignore          # Files excluded from Git
```

*Note: `dashboard.png` is generated when the dashboard script runs; it may not exist before the first successful run.*

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Quiz-Game-Management-System.git
```

### 2. Open the project folder

```bash
cd Quiz-Game-Management-System
```

### 3. Install dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

### 4. Start the quiz game

```bash
python main.py
```

### 5. Generate the dashboard

Choose the dashboard option from the main menu, or run:

```bash
python dashboard.py
```

The charts will be saved as `dashboard.png` in the project directory.

---

## 🎯 How to Use

1. Run `main.py`.
2. Register as a student if you do not already have a Student ID.
3. Select **Play Quiz** from the main menu.
4. Enter your registered Student ID.
5. Choose a quiz category and answer the multiple-choice questions.
6. View your score and check the leaderboard.
7. Open the visualization dashboard to analyze quiz performance.

**Important:** Existing registered students should use their saved Student IDs rather than registering again for every quiz.

---

## 📊 Data Visualization

The dashboard uses Matplotlib to convert stored quiz results into charts.

| Chart | What It Shows |
|---|---|
| Category Attempts | Number of attempts in each category |
| Score Distribution | Distribution of recorded scores |
| Top Performers | Students with the highest best scores |
| Activity Over Time | Quiz attempts grouped by date |

The charts make it easier to understand participation and performance trends at a glance.

---

## 🎓 Learning Outcomes

By developing this project, you can practice:

- Applying OOP principles to a real application.
- Implementing basic data structures and algorithms.
- Reading from and writing to CSV files.
- Building menu-driven applications in Python.
- Using Matplotlib for data visualization.
- Organizing a multi-file project.
- Publishing and maintaining code using GitHub.

---

## 🔮 Future Enhancements

- 🔐 Secure login and password management
- ⏱️ Timed quiz rounds
- 🗄️ SQL database integration
- 🌐 Web-based interface
- 📈 Detailed student performance analytics
- 🎯 Difficulty levels and randomized question selection
- 📝 Admin panel for managing questions and categories

---

## 👨‍💻 About the Project

**Quiz Game Management System** is an educational Python project developed to demonstrate the practical use of programming fundamentals, OOP, DSA, file handling, and data visualization in one application.

It is designed as a beginner-to-intermediate project for learning, academic demonstrations, and further development.

### ⭐ Support

If you find this project useful, consider giving the repository a **star** on GitHub!

---

*Built with Python 🐍 | Powered by DSA & Data Visualization 📊*
