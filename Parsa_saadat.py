import hashlib
import itertools

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def reverse_hash(hashed_password, wordlist):
    for word in wordlist:
        if hashlib.sha256(word.encode()).hexdigest() == hashed_password:
            return word
    return None

def generate_password_combinations(length):
    # Generates all possible combinations of passwords of a given length
    # For simplicity, let's assume only lowercase alphabets and digits are used
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    combinations = [''.join(x) for x in itertools.product(alphabet, repeat=length)]
    return combinations

def main():
    choice = input("Do you want to hash a password (h) or reverse a hash (r)? ")
    
    if choice == 'h':
        password = input("Enter your password: ")
        hashed_password = hash_password(password)
        print("Your hashed password is:", hashed_password)
    elif choice == 'r':
        hashed_password = input("Enter the hashed password: ")
        # Generating password combinations
        max_length = 8  # Set the maximum length of passwords to check
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