from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def build_car(self):
        i = random.choice([1, 2, 3, 4, 5, 6])
        if i == 4:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            new_y = random.randint(-220, 220)
            while new_y % 50 != 0:
                new_y = random.randint(-220, 220)
            new_car.goto(340, new_y)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_traffic(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def update_traffic(self):
        self.car_speed += MOVE_INCREMENT


