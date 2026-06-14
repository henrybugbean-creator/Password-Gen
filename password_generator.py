
import random
#global veriables for password generation
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
max = 20
#defult directory for saving passwords
default_directory = "passwords.txt"
#creates new password file with a header PASSWORDS if it doent exist
with open(default_directory, "w") as file:  
    file.write("PASSWORDS\n") 

#makes a totally random password at a give length with a mix of letters, digits and symbols
def random_password(length):
    #detects max length and returns None if length is greater than max
    if length > max:
        print("Password length exceeds maximum limit of 20 characters.")
        return None
    #password is ready to be generated
    password = ""
    #max a random password by randomly choosing letters, digits and symbols and shuffling them to make a random password
    password = random.choices(letters, k=max) + random.choices(digits, k=max) + random.choices(symbols, k=max) #make a password randomly with at most 20 letters, 20 digits and 20 symbols
    #lists then shuffles the password to make it random
    password_list = list(password)
    random.shuffle(password_list)
    #joins password back into a string
    password = "".join(password_list)
    #make the password the correct length by slicing it if it is longer than the desired length
    if len(password) > length:
        password = password[:length]
    #if all letters, digits and symbols are in the password then return the password
    if (letters in password) and (digits in password) and (symbols in password):
         
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

#while loop to simulate gui   
while True:
    #allows user to choose how to make their password and saves it to a file
    print("Choose how to make you password!")
    print("1. Generate a random password")
    print("2. Generate a personalized password")
    print("3. Make your own password")
    print("4. View saved passwords")
    print("5. Exit")
    #set directory to save passwords, if user does not input a directory then it will save to the default directory
    direcory = input("Enter the directory to save passwords (default is current directory): ")
    if direcory == "":
        direcory = default_directory
    #different choices
    choice = input("Enter your choice (1/2/3/4/5): ")
    if choice == "1":
        usecase = input("What is the password for: ")
        length = int(input("Enter the desired password length (max 20): "))
        password = random_password(length)
        if password:
            #opens file as the variable file with the append method
            with open(direcory, "a") as file:
                #write file usecase andq password to the file with a new line
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
        #opens file with read method as the variable file
        with open(direcory, "r") as file:
            #reads and turns file into list for a loop
            passwords = file.read().split("\n")
            #prints each password to a new line
            for password in passwords:
                print(password)
    elif choice == "5":
        print("Exiting the Password Generator. Goodbye!")
        break
    
    