# --------even and odd number------------
# number = int(input('enter a number: '))
# remainder = number % 2
# if remainder == 0:
#     print("Number is even")
# else:
#     print("Number is odd")


# ----------------rollercoaster------------------
# height = int(input("What is your height: "))
# if height > 120:
#     age = int(input("What is your age: "))
#     print("You can ride the rollercoaster!")
#     if age > 18:
#         print("Ticket cost: 50/-")
#     elif age > 12:
#         print("Ticket cost: 30/-")
#     else:
#         print("Ticket cost: 20/-")
# else:
#     print("You cant ride butkya..")


# ---------------BMI 2.0---------------------
# weight = float(input("What is your weight in Kg?\n"))
# height = float(input("What is your height in M?\n"))
# bmi = weight / (height ** 2)
# print("your BMI is "+str(round(bmi,2)))
# if bmi < 18.5:
#     print("you are underweight")
# elif bmi < 25:
#     print("You are normal weight")
# elif bmi < 30:
#     print("You are overweight")
# elif bmi < 35:
#     print("You are obese")
# else:
#     print("You are clinically obese")


# -------------Leap Year------------------
# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Its a leap year")
#         else:
#             print("Its not a leap year")
#     else:
#         print("Its a leap year")
# else:
#     print("Its not a leap year")


# --------------------Pizza bill----------------
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extracheese? Y or N: ")
# cost = 0
# if size == "S":
#     cost = 15
#     if add_pepperoni == "Y":
#         cost = cost + 2
# elif size == "M":
#     cost = 20
#     if add_pepperoni == "Y":
#         cost = cost + 3
# elif size == "L":
#     cost = 25
#     if add_pepperoni == "Y":
#         cost = cost + 3
# else:
#     print("Please choose correct size...")
#
# if extra_cheese == 'Y':
#     cost = cost + 1
#
# print(f"Your final bill is: ${cost}")


# ------------------Love Calculator--------------
# name1 = input("Enter your name: ")
# name2 = input("Enter your partners name: ")
# name1 = name1.lower()
# name2 = name2.lower()
# count1 = 0
# count2 = 0
# full_name = name1+name2
#
# count1 += full_name.count('t')
# count1 += full_name.count('r')
# count1 += full_name.count('u')
# count1 += full_name.count('e')
#
# count2 += full_name.count('l')
# count2 += full_name.count('o')
# count2 += full_name.count('v')
# count2 += full_name.count('e')
#
# score = int(str(count1)+str(count2))
#
# if score > 90 or score < 10:
#     print(f"Your score is {score}, you go together like coke and mentos.")
#
# elif 40 < score < 50:
#     print(f"Your score is {score}, you are alright together.")
#
# else:
#     print(f"Your score is {score}")


# ----------------------------if else story game-----------------------



print('''#


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::-'    `-::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::-'          `::::::::::::::::
:::::::::::::::::::::::::::::::::::::::-  '   /(_M_)\  `:::::::::::::::
:::::::::::::::::::::::::::::::::::-'        |       |  :::::::::::::::
::::::::::::::::::::::::::::::::-         .   \/~V~\/  ,:::::::::::::::
::::::::::::::::::::::::::::-'             .          ,::::::::::::::::
:::::::::::::::::::::::::-'                 `-.    .-::::::::::::::::::
:::::::::::::::::::::-'                  _,,-::::::::::::::::::::::::::
::::::::::::::::::-'                _,--:::::::::::::::::::::::::::::::
::::::::::::::-'               _.--::::::::::::::::::::::#####:::::::::
:::::::::::-'             _.--:::::::::::::::::::::::::::#####:::::####
::::::::'    ##     ###.-::::::###:::::::::::::::::::::::#####:::::####
::::-'       ###_.::######:::::###::::::::::::::#####:##########:::####
:'         .:###::########:::::###::::::::::::::#####:##########:::####
     ...--:::###::########:::::###:::::######:::#####:##########:::####
 _.--:::##:::###:#########:::::###:::::######:::#####:#################
'#########:::###:#########::#########::######:::#####:#################
:#########:::#############::#########::######:::#######################
##########:::########################::################################
##########:::##########################################################
##########:::##########################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################''')

print('\nWelcome to the Batman Challenge. \nYour mission is to find the treasure')

case1 = input('Would you like to take left lane or right lane? L or R: ')
if case1 == "L":
    print("Game over! You lost..HAHAHAA")
else:
    case2 = input('Would you fly over the mountain or go across it? F or A: ')
    if case2 == "A":
        print("Game over! You lost...")
    else:
        case3 = input("Would you wear a black suit, red suit or grey suit ? B, R, G: ")
        if case3 == 'B':
            print("Congratulations! You won the treasure!!!")
        else:
            print("Fuck off!")

