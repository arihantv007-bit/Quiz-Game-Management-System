import csv
import os
from collections import Counter
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(BASE, "quiz_results.csv")
OUTPUT = os.path.join(BASE, "dashboard.png")


def read_results():
    if not os.path.exists(RESULTS):
        return []
    with open(RESULTS, newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def main():
    results = read_results()
    if not results:
        print("No quiz results available.")
        print("Play at least one quiz before opening the dashboard.")
        return

    categories = Counter(row["category"] for row in results)
    ranges = {"0-39%": 0, "40-59%": 0, "60-79%": 0, "80-100%": 0}

    for row in results:
        percentage = float(row["percentage"])
        if percentage < 40:
            ranges["0-39%"] += 1
        elif percentage < 60:
            ranges["40-59%"] += 1
        elif percentage < 80:
            ranges["60-79%"] += 1
        else:
            ranges["80-100%"] += 1

    best_scores = {}
    for row in results:
        sid = row["student_id"]
        percentage = float(row["percentage"])
        if sid not in best_scores or percentage > best_scores[sid][1]:
            best_scores[sid] = (row["name"], percentage)

    top_students = sorted(
        best_scores.values(), key=lambda item: item[1], reverse=True
    )[:10]
    dates = Counter(row["date"] for row in results)
    average = sum(float(row["percentage"]) for row in results) / len(results)

    print("\n===== QUIZ ANALYTICS =====")
    print("Total Attempts:", len(results))
    print("Unique Students:", len(best_scores))
    print("Average Percentage:", round(average, 2), "%")

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    axes[0, 0].bar(categories.keys(), categories.values())
    axes[0, 0].set_title("Quiz Attempts by Category")
    axes[0, 0].set_ylabel("Attempts")

    labels = list(ranges.keys())
    values = list(ranges.values())
    axes[0, 1].pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    axes[0, 1].set_title("Score Distribution")

    names = [item[0] for item in top_students]
    scores = [item[1] for item in top_students]
    axes[1, 0].barh(names[::-1], scores[::-1])
    axes[1, 0].set_title("Top Students - Best Score")
    axes[1, 0].set_xlabel("Percentage")
    axes[1, 0].set_xlim(0, 100)

    sorted_dates = sorted(dates.items())
    axes[1, 1].plot(
        [item[0] for item in sorted_dates],
        [item[1] for item in sorted_dates],
        marker="o"
    )
    axes[1, 1].set_title("Quiz Attempts by Date")
    axes[1, 1].set_ylabel("Attempts")
    axes[1, 1].tick_params(axis="x", rotation=30)

    fig.suptitle("QUIZ GAME PERFORMANCE DASHBOARD", fontsize=15)
    plt.tight_layout()
    fig.savefig(OUTPUT, dpi=150, bbox_inches="tight")
    print("Graph saved successfully:", OUTPUT)
    plt.show()


if __name__ == "__main__":
    main()
