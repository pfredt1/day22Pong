import turtle
from turtle import Screen, Turtle
from paddle2 import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

start_x = 350
paddle_parts=[]
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
sleep_time = 0.2
while game_on:

    time.sleep(sleep_time)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if sleep_time >= .05:
            sleep_time *= .9


        print(sleep_time)


    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < - 380:
        ball.reset_ball()
        scoreboard.r_point()











screen.exitonclick()