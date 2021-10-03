from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
print(timmy)
screen.bgcolor("black")
timmy.shape("turtle")
timmy.color("blue")
timmy.fillcolor("white")
timmy.pencolor("white")
timmy.pensize(1)
timmy.speed(0)


screen.colormode(255)

def make_my_shape(sides):
    for _ in range(sides):
        timmy.forward(100)
        timmy.left(360 / sides)


def rand_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    timmy.pencolor(r, g, b)


def random_move():
    rand_move_list = ['l','r','f','b']
    move = random.choice(rand_move_list)
    if move == 'l':
        timmy.left(90)
        timmy.forward(50)
    if move == 'r':
        timmy.right(90)
        timmy.forward(50)
    if move == 'f':
        timmy.forward(50)
    else:
        timmy.backward(50)


# for times in range(500):
#     rand_color()
#     random_move()
#     # make_my_shape(times)


for _ in range(360//2):
    rand_color()
    timmy.left(2)
    timmy.circle(120)


screen.exitonclick()
