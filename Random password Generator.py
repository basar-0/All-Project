import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@$%^&*()_+")

print("Welcome to Password Generator")
n_letters = int(input("How many letters do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))

password = ""

for _ in range(n_letters):
    password += random.choice(letters)

for _ in range(n_numbers):
    password += random.choice(numbers)

for _ in range(n_symbols):
    password += random.choice(symbols)

password_list = list(password)
random.shuffle(password_list)

shuffle_password = "".join(password_list)
print("Your generated password is:", shuffle_password)