from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

## Challenge: list potential classes for the project
# screen of specific size
# paddle (that will create 2 paddle objects, allow for move, inherit from Turtle superclass)
# ball ('Turtle' for the ball, its speed increases after hit and discovery of 'hitting' the wall and the paddles
# scoreboard ( 2 scoreboard objects, for left and right paddle)
# possible class for the middle line - because its static and has no meaning can be left in main as another Turtle object


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0) # to make sure paddle animation from center is off

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
timer = 0.1


while game_is_on:
    time.sleep(timer)
    screen.update() # to make sure paddle animation from center is off
    ball.move_ball()
    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce
        ball.bounce_y()
    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        timer *= 0.9 # increase speed but never reach negative timer
        time.sleep(timer)
    # Detect when ball goes off the screen
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
        timer = 0.1
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
        timer = 0.1

screen.exitonclick()