# Student Management System

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks (space separated): ").split()))
    students[name] = marks
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        print(f"{name} -> Marks: {marks}, Average: {avg:.2f}")
    print()

def top_student():
    if not students:
        print("No data available.\n")
        return
    top = max(students, key=lambda x: sum(students[x]) / len(students[x]))
    avg = sum(students[top]) / len(students[top])
    print(f"Top Student: {top} with average {avg:.2f}\n")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Deleted successfully!\n")
    else:
        print("Student not found!\n")

def menu():
    while True:
        print("---- Student Management System ----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Top Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            top_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

menu()
