import hashlib
import os

def generate_password_hash(password):
    
    hash_object = hashlib.sha256(password.encode('utf-8'))
    password_hash = hash_object.hexdigest()
    return password_hash

def save_hash_to_file(password_hash):
    
    desktop_path = os.path.expanduser("~/Desktop")
    save_path = os.path.join(desktop_path, "password_hash.txt")

    with open(save_path, 'w') as file:
        file.write(password_hash)

def get_password_from_file(file_path):

    with open(file_path, 'r') as file:
        password_hash = file.read().strip()
    return password_hash


password = input("please code :")
password_hash = generate_password_hash(password)

save_hash_to_file(password_hash)

print("save file in desktop")
