from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5.0, stretch_len=1.0)
        self.color("white")
        self.goto(pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)