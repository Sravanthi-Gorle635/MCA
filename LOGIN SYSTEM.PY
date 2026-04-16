users = {}

def register():
    u = input("Username: ")
    p = input("Password: ")
    users[u] = p
    print("Registered!\n")

def login():
    u = input("Username: ")
    p = input("Password: ")

    if users.get(u) == p:
        print("Login successful!\n")
    else:
        print("Invalid credentials\n")

while True:
    print("1.Register 2.Login 3.Exit")
    ch = input("Choice: ")

    if ch == "1": register()
    elif ch == "2": login()
    elif ch == "3": break
