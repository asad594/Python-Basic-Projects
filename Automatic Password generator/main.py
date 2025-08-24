import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', ''
                                         'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input(f"How many symbols would you like?\n"))
no_of_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range(0, no_of_letters):
    password += random.choice(letters)

for char in range(0, no_of_symbols):
    password += random.choice(symbols)

for char in range(0, no_of_numbers):
    password += random.choice(numbers)

print(f"Without shuffle password is : {password}")
print("\n\n")
password = []
for char in range(0, no_of_letters):
    password.append(random.choice(letters))
for char in range(0, no_of_symbols):
    password.append(random.choice(symbols))
for char in range(0, no_of_numbers):
    password.append(random.choice(numbers))
print(f"Password in list is : {password}")
random.shuffle(password)
print(f"Shuffle password is : {password}")

password1 = ""
for i in password:
    password1 += i
print(f"The final password is: {password1}")

