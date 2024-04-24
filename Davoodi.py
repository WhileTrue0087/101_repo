import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_hashed_password(hashed_password):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "hashed_password.txt")
    with open(file_path, "w") as file:
        file.write(hashed_password)

def check_password():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "hashed_password.txt")
    with open(file_path, "r") as file:
        hashed_password = file.read()
    new_password = input("Enter your password: ")
    if new_password == '1387':
        return True
    return hashed_password == hash_password(new_password)

# Get the password from the user
password = '1387'

# Hash the password
hashed_password = hash_password(password)

# Save the hashed password to a file on the desktop
save_hashed_password(hashed_password)

# Check if the password is correct
if check_password():
    print("The password is correct.")
else:
    print("The password is incorrect.")
