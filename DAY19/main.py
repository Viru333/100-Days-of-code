import turtle as t
import random

# tim = t.Turtle()
screen = t.Screen()
# # def move_forward():
# #     tim.fd(10)
# #
# # screen.listen()
# # screen.onkey(key = "space", fun = move_forward)
#
#
# #ETCH A SKETCH
# # W --> FORWARD
# # S --> BACKWARD
# # A --> COUNTERCLOCKWISE
# # D --> CLOCKWISE
#
# def move_forward():
#     tim.fd(10)
#
# def move_backward():
#     tim.backward(10)
#
# def turn_right():
#     tim.setheading(tim.heading() - 10)
#
# def turn_left():
#     tim.setheading(tim.heading() + 10)
#
# def clear():
#     screen.resetscreen()
#
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")

colors = ["red", "blue", "green", "yellow", "orange", "violet", "indigo"]
y_pos = [-75, -45, -15, 15, 45, 75]
screen.setup(width=500, height=400)
is_race_on = False
all_turtles = []
user_bet = screen.textinput(title="make a bet", prompt="Which turtle will win the race? Enter a color: ")


def starting_position():
    for i in range(1,7):
        new_turtle = t.Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[i-1])
        new_turtle.goto(x=-230, y=y_pos[i-1])
        all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

starting_position()

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won. The {winning_color} turtle won the race.")
            else:
                print(f"You've lost. The {winning_color} turtle won the race.")
            is_race_on = False
            break

        d = random.randint(1, 10)
        turtle.fd(d)



screen.exitonclick()