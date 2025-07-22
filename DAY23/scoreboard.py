from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME-OVER", False, "center", FONT)
        # self.goto(0, 0)

