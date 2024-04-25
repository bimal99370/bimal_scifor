import random

def generate_random_password(length = 10):
    password = ""
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

    while len(password) < length:
        password += random.choice(characters)

    return password

random_password = generate_random_password()
print("The Random Password is :", random_password)
