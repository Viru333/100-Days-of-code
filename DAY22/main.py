from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)


r_pos = (350, 0)
l_pos = (-350, 0)
Right_paddle = Paddle(r_pos)
Left_paddle = Paddle(l_pos)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Right_paddle.go_up, "Up")
screen.onkey(Right_paddle.go_down, "Down")
screen.onkey(Left_paddle.go_up, "w")
screen.onkey(Left_paddle.go_down, "s")


is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()s
    scoreboard.update()
    ball.move()

    # Detect collision with wall and change direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with r_paddle
    if ball.distance(Right_paddle) < 50 and ball.xcor() > 320 or ball.distance(Left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect Right_paddle Misses
    if ball.xcor() > 380:
        ball.next_row()
        scoreboard.l_point()

    # Detect Left_paddle Misses
    if ball.xcor() < -380:
        ball.next_row()
        scoreboard.r_point()

























screen.exitonclick()