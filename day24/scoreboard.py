from turtle import Turtle
with open('day24/data.txt') as file:
    highest_score = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=270)
        self.score = 0
        self.high_score = int(highest_score)
        self.display()

    def display(self):
        self.clear()
        disp = f"Scores: {self.score} High Score: {self.high_score}"
        self.write(arg= disp, align="center",font=("san", 20, "normal"))

    def scoreup(self):
        self.score += 1
        self.display()

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('day24/data.txt', mode='w') as hs:
                hs.write(str(self.high_score))
        self.score = 0
        self.display()
