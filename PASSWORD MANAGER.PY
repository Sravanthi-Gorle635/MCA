import json
import base64
from cryptography.fernet import Fernet

# Generate key (run once and save it)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

# Load key
def load_key():
    return open("key.key", "rb").read()

# Encrypt password
def encrypt_password(password, key):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

# Decrypt password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

# Load data
def load_data():
    try:
        with open("passwords.json", "r") as f:
            return json.load(f)
    except:
        return {}

# Save data
def save_data(data):
    with open("passwords.json", "w") as f:
        json.dump(data, f, indent=4)

def add_password():
    site = input("Enter site: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    key = load_key()
    encrypted = encrypt_password(password, key)

    data = load_data()
    data[site] = {"username": username, "password": encrypted}
    save_data(data)

    print("Password saved securely!\n")

def view_password():
    site = input("Enter site: ")
    data = load_data()

    if site in data:
        key = load_key()
        decrypted = decrypt_password(data[site]["password"], key)
        print(f"Username: {data[site]['username']}")
        print(f"Password: {decrypted}\n")
    else:
        print("No data found!\n")

def menu():
    while True:
        print("1. Add Password")
        print("2. View Password")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice\n")

# Run first time
try:
    load_key()
except:
    print("Generating encryption key...")
    generate_key()

menu()
