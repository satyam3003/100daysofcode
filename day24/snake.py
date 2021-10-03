from turtle import *
import random
COLOR_CHOICE = ['red','green','white','blue','yellow','pink','brown']
BODY_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
screen = Screen()
colormode(255)

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for x in BODY_POSITIONS:
            self.add_segment(x)

    def add_segment(self,position):
        snake = Turtle(shape='square')
        snake.penup()
        snake.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        snake.goto(position)
        self.segments.append(snake)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].xcor(), self.segments[seg - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def snake_restart(self):
        for snake in self.segments:
            snake.reset()
        self.segments = []
        self.create_snake()
