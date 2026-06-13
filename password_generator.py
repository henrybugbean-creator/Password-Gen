import random

def random_password(length):
    
    password = ""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    while len(password) != length:
        password = random.choices(letters, k=random.randint(1, 4)) + random.choices(digits, k=random.randint(1, 4)) + random.choices(symbols, k=random.randint(1, 4))
        if len(password) > length:
            password = password[:length]

        if (letters in password) and (digits in password) and (symbols in password):
            break

        
        
    return "".join(password)
password = random_password(9)
print(password)

def personalized_password(length, name):
    password = random_password(length)
    personalized = list(password[length//2:] + name + password[:length//2])
    return "".join(personalized)
    

print(personalized_password(9, input("Enter your name: ")))

