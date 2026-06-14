import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
max = 20

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
password = random_password(9)
print(password)

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
    

print(personalized_password(9, input("Enter your name: ")))
