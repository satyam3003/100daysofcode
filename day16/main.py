# -------------- Turtle ----------------
# import turtle
#
# screen = turtle.Screen()
# screen.bgcolor('black')
# print(screen.canvwidth)
# sam = turtle.Turtle()
# sam.shape('turtle')
# sam.color("white")
# sam.fillcolor('blue')
# for _ in range(4):
#     sam.forward(100)
#     sam.right(45)
#     sam.circle(50)
#     sam.left(45)
#     sam.right(90)
# screen.exitonclick()


# ----------------- Pretty table -----------------
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_names = ["Pokemon Name   ","Type"]
# table.add_rows([["Pikachu","fire"],["Raichu","fire"],["Bulbasor","Water"]])
# table.align = 'l'
# table.sortby = 'Type'
# print(table)


# -------------------- Coffee Machine ----------------
# https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    order = input(f"What would you like? {options}")
    if order == 'off':
        is_on = False
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        my_drink = menu.find_drink(order)
        Check_flag = coffee_maker.is_resource_sufficient(my_drink)
        if Check_flag:
            if money_machine.make_payment(my_drink.cost):
                coffee_maker.make_coffee(my_drink)









