# ---------bmi calc-----------
# weight = float(input("What is your weight in Kg?\n"))
# height = float(input("What is your height in M?\n"))
# bmi = weight // (height ** 2)
# print("your BMI is "+str(bmi))

# ---------remaining age----------
# yourage = int(input("Your age in years: "))
# difference = 90 - yourage
# years = difference
# days = difference*365
# weeks = difference * 52
# months = difference*12
# print(f"you have {days} days {weeks} weeks {months} months {years} years left")


# ----------------split bill challenge-----------
print("Welcome to the split calculator")
bill = float(input("Enter total bill: "))
tip_perc = float(input("Enter tip in %: "))
people = int(input("Enter no. of people to split bill: "))
tip = bill * (tip_perc / 100)
total_bill = bill + tip
personal_bill = round(total_bill/people)
print(f"Each person should pay ₹{personal_bill}")



