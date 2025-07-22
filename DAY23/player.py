from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_pos()

    def cross_road(self):
        self.fd(25)

    def crossed_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def reset_pos(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)