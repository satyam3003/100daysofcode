# ----------------Average of height --------------
# heights = [140, 130, 150, 125, 180, 100, 165, 132, 189]
# total = 0
# counter = 0
# for height in heights:
#     total += height
#     counter += 1
#
# print(total)
# average = total / counter
# print(counter)
# print(average)


# ----------------Highest score-------------
# scores = [90,80,45,57,89,25,99,86]
# highscore = 0
# for score in scores:
#     if score > highscore:
#         highscore = score
#
# print(highscore)


# --------addition of 1 to 100-------------
# total = 0
# for number in range(1,101):
#     total += number
# print(total)


# ----------addition of even no between 1 to 100-----------
# total = 0
# for number in range(2,101,2):
#     total += number
# print(total)

# -------------fizzbuzz game-----------------
# for number in range(1,101):
#     if number%3 == 0 and number % 5 ==0:
#         print('fizzbuzz')
#     elif number%3 == 0:
#         print('fizz')
#     elif number%5 == 0:
#         print('buzz')
#     else:
#         print(number)


# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_final = ''

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for password in range(0,nr_letters):
    p1 = letters[random.randint(0, len(letters) - 1)]
    password_final = password_final + p1

for password in range(0,nr_symbols):
    p2 = symbols[random.randint(0, len(symbols) - 1)]
    password_final = password_final + p2

for password in range(0,nr_numbers):
    p3 = numbers[random.randint(0, len(numbers) - 1)]
    password_final = password_final + p3
print(f"Easy password: {password_final}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

phard = []
final_hard_password = ''

for passhard_ind in range(0, len(password_final)):
    phard.append(password_final[passhard_ind])

random.shuffle(phard)

for char in range(0, len(password_final)):
    final_hard_password = final_hard_password + phard[char]

print(f"Hard password: {final_hard_password}")