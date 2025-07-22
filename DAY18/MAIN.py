import turtle
from turtle import Turtle, Screen
import random
import colorgram
#import turtle as t

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("square")
# timmy_the_turtle.color("red")
#
# for _ in range(4):
#     timmy_the_turtle.fd(100)
#     timmy_the_turtle.right(90)

tim  = Turtle()

# for _ in range(50):
#     if(tim.isdown()):
#         tim.penup()
#     else:
#         tim.pendown()
#     tim.forward(10)

#draw triangle

# for i in range(3,11):
#     side = i
#     angle = 360/i
#
#     while side:
#         tim.right(angle)
#         tim.forward(100)
#         side -= 1


#random walk
turtle.colormode(255)
colors = colorgram.extract('maxresdefault.jpg', 20)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    this_tuple = (r,g,b)
    return this_tuple

def random_walk():
    tim.pensize(10)
    directions = [0,90,180,270]
    tim.speed("fast")

    for _ in range(200):
        d = random.choice(directions)
        tim.color(random_color())
        tim.fd(30)
        tim.setheading(d)

def spirograph(size_of_gap):
    tim.speed(0)
    for _ in range(int(360/size_of_gap)):
        tim.color(random.choice(colors).rgb)
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

# spirograph(2)

def hirst_dot_painting(dot_size, length, height):
    tim.speed(0)
    tim.penup()
    tim.hideturtle()
    for h in range(0,height+1):
        p = tim.position()
        for l in range(0,length+1):
            tim.color(random.choice(colors).rgb)
            tim.dot(dot_size)
            tim.penup()
            tim.fd(5*length)

        tim.setpos(p)
        tim.setheading(90)
        tim.fd(5*length)
        tim.setheading(0)

hirst_dot_painting(20,10,10)

screen = Screen()
screen.exitonclick()

