from turtle import Turtle

position = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
snake_size = 20
snake_color = "white"


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in position:
            self.add_segment(tuple(i))

    def add_segment(self, pos):
        new_turtle = Turtle(shape="square")
        new_turtle.color(snake_color)
        new_turtle.pensize(snake_size)
        new_turtle.penup()
        new_turtle.goto(pos)
        self.segments.append(new_turtle)

    def extend_segment(self):
        pos = self.segments[-1].pos()
        self.add_segment(pos)

    def move(self):

        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)


