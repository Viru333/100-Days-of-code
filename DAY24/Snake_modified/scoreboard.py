from turtle import Turtle
from food import Food

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.f = open("data.txt")
        self.high_score = int(self.f.read())
        self.f.close()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.show_score()

    def refresh(self):
        self.score += 1
        self.clear()
        self.show_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.show_score()


    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)