import datetime

attendance = {}

def mark_attendance():
    name = input("Enter student name: ")
    date = str(datetime.date.today())

    if date not in attendance:
        attendance[date] = []

    attendance[date].append(name)
    print("Attendance marked!\n")

def view_attendance():
    for date, names in attendance.items():
        print(date, ":", names)
    print()

while True:
    print("1.Mark Attendance 2.View Attendance 3.Exit")
    ch = input("Choice: ")

    if ch == "1": mark_attendance()
    elif ch == "2": view_attendance()
    elif ch == "3": break
