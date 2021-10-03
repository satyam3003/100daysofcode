import random


# How to use a module and random module
# import my_module
#
#
# print(random.random(), random.randint(0, 10))
# print(my_module.pi)


# -----------Heads and Tails generator
# number = random.randint(0,1)
# if number == 0:
#     print("Heads")
# else:
#     print("Tails")


# ---------------Understanding List-----------------
# fruits = ["Apple","Banana","Mango","Chikko","Grapes","Apple"]
# print(fruits)
#
# print(fruits[0])
#
# fruits.append("Guava")
# print(fruits)
#
# fruits.sort()
# print(fruits)
#
# fruits.reverse()
# print(fruits)
#
# print(fruits.count("Apple"))
#
# fruits.extend(["Mango","Papaya"])
# print(fruits)


# ----------------------Who will pay the bill ---------------------
# import random
# name_string = input("Enter all names seperated by , :")
# names = name_string.split(", ")
# index = random.randint(0, len(names)-1)
# print(f"{names[index]} will pay bill today")


# -----------------Game------------------
# row1 = ['💚','💛','💛']
# row2 = ['💚','💛','💛']
# row3 = ['💚','💛','💛']
# base_chart = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input('Enter your position: (column then row): ')
# list_no = int(position[1]) - 1
# item_no = int(position[0]) - 1
# print(list_no,item_no)
# base_chart[list_no][item_no] = 'X'
# print(f"{row1}\n{row2}\n{row3}")


# rock paper scissors
import random
print('Welcome to rock paper Scissors!!!!!!!!!!')
user_input = input("Rock Paper Scissor? R, P, S: ")
options = ['R','P','S']
comp_input = options[random.randint(0, len(options)-1)]
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if user_input == 'R':
    print("Your input:")
    print(rock)
elif user_input == 'P':
    print("Your input:")
    print(paper)
elif user_input == 'S':
    print("Your input:")
    print(scissors)
else:
    print("Invalid input")
    exit()
if comp_input == 'R':
    print("Comp input:")
    print(rock)
elif comp_input == 'P':
    print("Comp input:")
    print(paper)
elif comp_input == 'S':
    print("Comp input:")
    print(scissors)


if comp_input == user_input:
    print("its a draw")
elif comp_input == 'R' and user_input == "P":
    print("You Won!")
elif comp_input == 'R' and user_input == "S":
    print("You Lost")
elif comp_input == 'P' and user_input == "S":
    print("You Won!")
elif comp_input == 'P' and user_input == "R":
    print("You Lost")
elif comp_input == 'S' and user_input == "R":
    print("You Won!")
elif comp_input == 'S' and user_input == "P":
    print("You Lost")
