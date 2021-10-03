from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()


def move():
    tim.forward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def clear():
    tim.reset()


def circle():
    tim.circle(50)

screen.listen()
screen.onkey(forward, "w")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(backward, "s")
screen.onkey(circle, "z")
screen.onkey(clear, "c")
screen.exitonclick()