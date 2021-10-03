from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up,'Up')
screen.onkey(r_paddle.move_down,'Down')
screen.onkey(l_paddle.move_up,'w')
screen.onkey(l_paddle.move_down,'s')

score = Scoreboard()
ball_speed = 0.1
screen_is_on = True
while screen_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.deflection()

    if r_paddle.distance(ball) < 50 and ball.xcor() > 320 or l_paddle.distance(ball) < 50 and ball.xcor()<-320:
        ball.reverse()

    if ball.xcor() > 390:
        time.sleep(0.4)
        ball_speed *= 0.9
        ball.ballrestart()
        score.display('l')

    if ball.xcor() < -390:
        time.sleep(0.4)
        ball_speed *= 0.9
        ball.ballrestart()
        score.display('r')


screen.exitonclick()