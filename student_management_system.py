import csv
import os

FILE_NAME = "students.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Course", "Marks"])


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, course, marks])

    print("Student Added Successfully!")


def view_students():
    print("\n===== STUDENT RECORDS =====\n")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def search_student():
    student_id = input("Enter Student ID: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] == student_id:
                print("\nStudent Found:")
                print(row)
                found = True

    if not found:
        print("Student Not Found.")


def update_student():
    student_id = input("Enter Student ID to Update: ")

    rows = []
    updated = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] == student_id:
                row["Name"] = input("Enter New Name: ")
                row["Course"] = input("Enter New Course: ")
                row["Marks"] = input("Enter New Marks: ")
                updated = True

            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["ID", "Name", "Course", "Marks"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    if updated:
        print("Student Updated Successfully!")
    else:
        print("Student Not Found.")


def delete_student():
    student_id = input("Enter Student ID to Delete: ")

    rows = []
    deleted = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] != student_id:
                rows.append(row)
            else:
                deleted = True

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["ID", "Name", "Course", "Marks"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    if deleted:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found.")


def main():
    initialize_file()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank You For Using Student Management System!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()