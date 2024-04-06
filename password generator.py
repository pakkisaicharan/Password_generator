import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_passwords(num_passwords, length):
    passwords = []
    for _ in range(num_passwords):
        passwords.append(generate_password(length))
    return passwords

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the length of each password: "))
    if num_passwords <= 0 or length <= 0:
        print("Number of passwords and length should be greater than 0.")
        return

    passwords = generate_passwords(num_passwords, length)
    print("Generated Passwords:")
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()

