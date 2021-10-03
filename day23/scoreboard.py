from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=260)
        self.level = 1
        self.display()

    def display(self):
        self.clear()
        disp = f"Level: {self.level}"
        self.write(arg=disp, align="left", font=FONT)

    def update_score(self):
        self.level += 1
        self.display()

    def endgame(self):
        end = Turtle()
        end.color("black")
        end.penup()
        end.hideturtle()
        end.write(arg = "Game Over", align='center',font=FONT)



