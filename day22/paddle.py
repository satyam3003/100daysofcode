from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 5)
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.resizemode("user")
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)