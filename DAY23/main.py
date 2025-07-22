import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.cross_road, "Up")

# time_pause = 0
# val = 20
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.build_car()
    cars.move_traffic()
    # time_pause += 1

    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.crossed_finish_line():
        scoreboard.update_score()
        player.reset_pos()
        cars.update_traffic()
        # time_pause = 0
        # val -= 1


screen.exitonclick()

