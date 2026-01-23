# Data Visualizer Project
# Pure Python (Standard Library Only)
# Works on Windows, Linux, macOS

import csv
import math
import os


def read_marks(filename):
    """Read CSV file safely using absolute path"""
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)

    data = []
    with open(file_path, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def calculate_stats(data):
    """Calculate mean, median, and standard deviation"""
    marks = [int(row['marks']) for row in data]
    marks.sort()
    n = len(marks)

    mean = sum(marks) / n

    if n % 2 == 0:
        median = (marks[n // 2 - 1] + marks[n // 2]) / 2
    else:
        median = marks[n // 2]

    variance = sum((x - mean) ** 2 for x in marks) / n
    std_dev = math.sqrt(variance)

    return mean, median, std_dev, marks


def generate_report(data, stats):
    """Generate ASCII visualization report (UTF-8 safe)"""
    mean, median, std_dev, marks = stats
    base_dir = os.path.dirname(__file__)
    report_path = os.path.join(base_dir, "report.txt")

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("CLASS PERFORMANCE REPORT\n")
        file.write("=" * 30 + "\n\n")

        file.write(f"Mean Marks   : {mean:.2f}\n")
        file.write(f"Median Marks : {median:.2f}\n")
        file.write(f"Std Deviation: {std_dev:.2f}\n\n")

        file.write("MARKS DISTRIBUTION (ASCII BAR CHART)\n")
        file.write("-" * 30 + "\n")

        for mark in sorted(set(marks)):
            count = marks.count(mark)
            file.write(f"{mark:3d} | {'█' * count}\n")


def main():
    print("📊 Running Data Visualizer...\n")

    data = read_marks("student_marks.csv")
    stats = calculate_stats(data)
    generate_report(data, stats)

    print("✅ Report generated successfully!")
    print("📄 Output file: report.txt")


if __name__ == "__main__":
    main()
