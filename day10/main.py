# -------------- function which returns a value -------------
# def my_function(f_name, l_name):
#     full_name = f_name + " " + l_name
#     return full_name.title()
#
#
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# full = my_function(first_name,last_name)
# print(full)


# ------------- days in month finder --------
# def is_leap(year_check):
#     if year_check % 4 == 0:
#         if year_check % 100 == 0:
#             if year_check % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(current_year, current_month):
#     leap = is_leap(current_year)
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if leap == True:
#         month_days[1] = 29
#
#     return month_days[current_month-1]
#
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# -------------- Calculator ------------

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


num1 = float(input("enter number 1: "))

continue_calc = True
while continue_calc:
    sign = input("Enter command { + , - , * , / }: ")
    num2 = float(input("enter number 2: "))

    operations = {
        '+': add,
        '-': sub,
        '*': mult,
        '/': div,
    }
    if sign == operations:
        print(True)

    op_select = operations[sign]
    result = op_select(num1, num2)

    print(f"output: {num1} {sign} {num2} = {result}")
    num1 = result

    cont = input("Type exit to exit / press enter to continue: ")
    if cont == 'exit':
        continue_calc = False
