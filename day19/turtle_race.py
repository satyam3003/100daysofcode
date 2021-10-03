from turtle import Turtle,Screen
import random

game_on = False
screen = Screen()
screen.setup(500,400)
colors = ['red', 'green', 'blue' , 'pink', 'black', 'orange']
y_pos = 100
my_turtles = []

for turtle_index in range(6):
    turtle1 = Turtle(shape="turtle")
    turtle1.penup()
    turtle1.color(colors[turtle_index])
    turtle1.goto(-230, y_pos)
    y_pos -= 40
    my_turtles.append(turtle1)

print(my_turtles)
user_bet = screen.textinput("Pick your bet", "Who will win the race")
if user_bet != '':
    game_on = True

while game_on:
    for turt in my_turtles:
        if turt.xcor() > 230:
            game_on = False
            winner = turt.color()[0]
            if winner == user_bet:
                print("you won")
            else:
                print("you lost")

        turt.forward(random.randint(0,10))

screen.exitonclick()
