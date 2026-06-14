
import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
max = 20
with open("passwords.txt", "w") as file:  
    file.write("PASSWORDS\n")  # Create the file if it doesn't exist
def random_password(length):
    if length > max:
        print("Password length exceeds maximum limit of 20 characters.")
        return None
    password = ""
    while len(password) != length:
        password = random.choices(letters, k=random.randint(1, 4)) + random.choices(digits, k=random.randint(1, 4)) + random.choices(symbols, k=random.randint(1, 4))
        password_list = list(password)
        random.shuffle(password_list)
        password = "".join(password_list)
        if len(password) > length:
            password = password[:length]

        if (letters in password) and (digits in password) and (symbols in password):
            break
    return "".join(password)


def personalized_password(length, name):
    if length > max:
        print("Password length exceeds maximum limit of 20 characters.")
        return None
    if len(name) >= length:
        personalised = name + random.choices(letters + digits + symbols, k=random.randint(4, 6))
        
    else:
        password = random_password(length)
        personalised = list(password[length//2:] + name + password[:length//2])
    return "".join(personalised)
    
while True:
    print("Welcome to the Password Generator!")
    print("1. Generate a random password")
    print("2. Generate a personalized password")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        usecase = input("What is the password for: ")
        length = int(input("Enter the desired password length (max 20): "))
        password = random_password(length)
        if password:
            with open("passwords.txt", "a") as file:
                file.write(f"{usecase} = {password}\n")
    elif choice == "2":
        usecase = input("What is the password for: ")
        length = int(input("Enter the desired password length (max 20): "))
        name = input("Enter your name: ")
        password = personalized_password(length, name)
        if password:
            with open("passwords.txt", "a") as file:
                file.write(f"{usecase} = {password}\n")
    elif choice == "3":
        print("Exiting the Password Generator. Goodbye!")
        break
    
    