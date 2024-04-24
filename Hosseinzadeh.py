import hashlib
import itertools

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def reverse_hash(hashed_password, wordlist):
    return next((word for word in wordlist if hashlib.sha256(word.encode()).hexdigest() == hashed_password), None)

def generate_password_combinations(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return [''.join(x) for x in itertools.product(alphabet, repeat=length)]

def main():
    choice = input("Do you want to hash a password (h) or reverse a hash (r)? ")
    
    if choice == 'h':
        password = input("Enter your password: ")
        hashed_password = hash_password(password)
        print("Your hashed password is:", hashed_password)
    elif choice == 'r':
        hashed_password = input("Enter the hashed password: ")
        max_length = 8
        for length in range(1, max_length + 1):
            password_combinations = generate_password_combinations(length)
            original_password = reverse_hash(hashed_password, password_combinations)
            if original_password:
                print("The original password is:", original_password)
                break
        else:
            print("Password not found in the generated combinations.")

if __name__ == "__main__":
    main()