# Mohammad Omid Azizi

import hashlib

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(stored_password_hash, user_password):
    """Verify a stored password against one provided by user."""
    return stored_password_hash == hash_password(user_password)

# Input password from user
password = input("Enter your password: ")
password_hash = hash_password(password)
print("Password hash saved.")

# Check if the inputted user password is correct
password_to_check = input("Re-enter your password to check: ")
if verify_password(password_hash, password_to_check):
    print("Password is correct.")
else:
    print("Password is incorrect.")
