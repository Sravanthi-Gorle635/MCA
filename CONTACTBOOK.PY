contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    print("Contact saved!\n")

def view_contacts():
    for name, phone in contacts.items():
        print(f"{name} - {phone}")
    print()

def search_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Not found\n")

def delete_contact():
    name = input("Enter name to delete: ")
    contacts.pop(name, None)

while True:
    print("1.Add 2.View 3.Search 4.Delete 5.Exit")
    ch = input("Choice: ")

    if ch == "1": add_contact()
    elif ch == "2": view_contacts()
    elif ch == "3": search_contact()
    elif ch == "4": delete_contact()
    elif ch == "5": break
