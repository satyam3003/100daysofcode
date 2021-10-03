import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_left,"Left")
screen.onkey(player.move_down,"Down")
screen.onkey(player.move_right,"Right")

carmanager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_chance = random.randint(1,6)
    if random_chance == 1:
        carmanager.new_car()
    carmanager.move_cars()
    if player.ycor() > 280:
        player.game_reset()
        scoreboard.update_score()
        carmanager.speedup()

    for car in carmanager.all_cars:
        if car.distance(player) < 20 + carmanager.car_speed //2:
            game_is_on = False
            scoreboard.endgame()


screen.exitonclick()



