
import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
max = 20
default_directory = "passwords.txt"
with open("passwords.txt", "w") as file:  
    file.write("PASSWORDS\n")  # Create the file if it doesn't exist
def random_password(length):
    if length > max:
        print("Password length exceeds maximum limit of 20 characters.")
        return None
    password = ""
    while len(password) != length:
        password = random.choices(letters, k=max) + random.choices(digits, k=max) + random.choices(symbols, k=max)
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
        personalised = name + str(random.choices(letters + digits + symbols, k=random.randint(4, 6)))
        
    else:
        password = random_password(length)
        personalised = list(password[length//2:] + name + password[:length//2])
    return "".join(personalised)
    
while True:
    print("Choose how to make you password!")
    print("1. Generate a random password")
    print("2. Generate a personalized password")
    print("3. Make your own password")
    print("4. View saved passwords")
    print("5. Exit")
    direcory = input("Enter the directory to save passwords (default is current directory): ")
    if direcory == "":
        direcory = default_directory
    choice = input("Enter your choice (1/2/3/4/5): ")
    if choice == "1":
        usecase = input("What is the password for: ")
        length = int(input("Enter the desired password length (max 20): "))
        password = random_password(length)
        if password:
            with open(direcory, "a") as file:
                file.write(f"{usecase} = {password}\n")
    elif choice == "2":
        usecase = input("What is the password for: ")
        length = int(input("Enter the desired password length (max 20): "))
        name = input("Enter your name: ")
        password = personalized_password(length, name)
        if password:
            with open(direcory, "a") as file:
                file.write(f"{usecase} = {password}\n")
    elif choice == "3":
        usecase = input("What is the password for: ")
        password = input("Enter your own password: ")
        with open(direcory, "a") as file:
            file.write(f"{usecase} = {password}\n")
    elif choice == "4":
        with open(direcory, "r") as file:
            passwords = file.read().split("\n")
            for password in passwords:
                print(password)
    elif choice == "5":
        print("Exiting the Password Generator. Goodbye!")
        break
    
    