import re

def check_password(password):
    strength = "Weak"

    if (len(password) >= 8 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[@#$%^&+=]", password)):
        strength = "Strong"
    elif len(password) >= 6:
        strength = "Medium"

    return strength

pwd = input("Enter password: ")
print("Strength:", check_password(pwd))
