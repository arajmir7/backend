import os
from utils.file_handler import FileHandler
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "students.json")

handler = FileHandler(DATA_FILE)


def display_students(students):
    if not students:
        print("No records found.")
        return

    for s in students:
        print(f"{s['id']} | {s['name']} | {s['course']} | {s['created_at']}")


def add_student(students):
    sid = input("Student ID: ").strip()
    name = input("Name: ").strip()
    course = input("Course: ").strip()

    students.append({
        "id": sid,
        "name": name,
        "course": course,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


def delete_student(students):
    sid = input("Enter ID to delete: ").strip()
    students[:] = [s for s in students if s["id"] != sid]


def update_student(students):
    sid = input("Enter ID to update: ").strip()

    for s in students:
        if s["id"] == sid:
            s["name"] = input("New name: ").strip()
            s["course"] = input("New course: ").strip()
            return

    print("Student not found.")


def main():
    students = handler.load_data()

    while True:
        print("\n--- Student File System ---")
        print("1. View students")
        print("2. Add student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Save & Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            display_students(students)

        elif choice == "2":
            add_student(students)

        elif choice == "3":
            update_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            if handler.save_data(students):
                print("✅ Data saved safely.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
