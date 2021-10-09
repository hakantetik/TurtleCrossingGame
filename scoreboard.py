from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update()

    def update(self):
        self.goto(-270, 250)
        self.color("black")
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def score(self):
        self.clear()
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align="center", font=FONT)
