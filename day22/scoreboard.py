from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=240)
        self.score_l = -1
        self.score_r = -1
        self.display(sides='start')

    def display(self, sides):
        self.clear()
        if sides == 'r':
            self.score_r += 1
        if sides == 'l':
            self.score_l += 1
        if sides == 'start':
            self.score_l += 1
            self.score_r += 1

        disp = f"Scores\n {self.score_l}    {self.score_r}"
        self.write(arg= disp, align="center",font=("san", 20, "normal"))
