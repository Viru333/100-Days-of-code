#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8,10)
nr_numbers = random.randint(2,4)
nr_symbols = random.randint(2,4)

password_list = []

for i in range(nr_letters):
    password_list += random.choice(letters)

for i in range(nr_numbers):
    password_list += random.choice(numbers)

for i in range(nr_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""

for i in password_list:
    password += i
print(f"Here is your Password: {password}.")



