from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.width(15)
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x , new_y)

    def deflection(self):
        self.y_move = -1 * self.y_move

    def reverse(self):
        self.x_move = -1 * self.x_move

    def ballrestart(self):
        self.goto(0,0)
        self.reverse()
        self.move()
