from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.color('black')
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)

    def move_down(self):
        new_x = self.xcor()
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(new_x, new_y)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def game_reset(self):
        self.goto(STARTING_POSITION)