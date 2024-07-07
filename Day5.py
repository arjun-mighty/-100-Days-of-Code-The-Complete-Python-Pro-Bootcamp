#Password Generator Easy Level
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password Generator !")
num_letters=int(input("How many letters would you like to have in your password?\n"))
num_symbols=int(input("How many symbols would you like?\n"))
num_numbers=int(input("How many numbers would you like?\n"))


password = ""
for char in range(1,num_letters+1):
    password += random.choice(letters)

for char in range(1,num_symbols+1):
    password += random.choice(symbols)

for char in range(1,num_numbers+1):
    password += random.choice(numbers)

print(f"Here is your password:{password}")

# ---------------End-----------------
#Password Generator Hard Level
#Password Generator using list
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password Generator !")
num_letters=int(input("How many letters would you like to have in your password?\n"))
num_symbols=int(input("How many symbols would you like?\n"))
num_numbers=int(input("How many numbers would you like?\n"))


password_list = []
for char in range(1,num_letters+1):
    password_list.append(random.choice(letters))

for char in range(1,num_symbols+1):
    password_list+= random.choice(symbols)

for char in range(1,num_numbers+1):
    password_list += random.choice(numbers)

print(f"Here is your password:{password_list}")
random.shuffle(password_list)
print(f"Here is your password:{password_list}")

password = ""
for char in password_list:
    password+=char
print(f"Here is your password:{password}")
    
  