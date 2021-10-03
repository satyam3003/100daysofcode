from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=270)
        self.score = -1
        self.display()
        self.high_score = 0

    def display(self):
        self.clear()
        disp = f"Scores: {self.score} HighScore: {self.high_score}"
        self.write(arg= disp, align="center",font=("san", 20, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        disp = f"Game Over! Your Score: {self.score}"
        self.write(arg=disp, align="center", font=("san", 20,"normal"))

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display()

    def score_update(self):
        self.score += 1
        self.display()