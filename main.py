from turtle import Screen
from time import sleep
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()



screen.onkeypress(fun=player.move, key="Up")

game_is_on = True

while game_is_on:
    sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()
    if player.ycor() >= 280:
        scoreboard.score()
        car_manager.level_up()
        player.goto(0, -200)

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False






screen.exitonclick()
