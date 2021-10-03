import turtle as tur
import colorgram
import random

# bald = colorgram.extract('day18/color_pallet.jpg', 20)
# rgb_list = []
# for item in range(20):
#     r = bald[item].rgb.r
#     g = bald[item].rgb.g
#     b = bald[item].rgb.b
#     rgb_list.append((r, g, b))

rgb_list = [ (236, 35, 108), (145, 28, 64), (239, 75, 35),
            (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195),
            (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165),
            (215, 56, 27)]

timmy = tur.Turtle()

timmy.hideturtle()
timmy.penup()
timmy.setx(250)
timmy.sety(-250)
timmy.pensize(25)
timmy.shape("turtle")
tur.colormode(255)

for y in range(10):
    timmy.speed(0)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    for rev_x in range(10):
        timmy.forward(50)
    timmy.left(180)
    timmy.speed(5)
    for x in range(10):
        timmy.forward(50)
        timmy.dot(20, random.choice(rgb_list))

screen = tur.Screen()
screen.exitonclick()
