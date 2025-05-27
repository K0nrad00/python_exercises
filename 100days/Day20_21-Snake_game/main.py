from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # turn off animation for smooth snake movement

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen() # listen for keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() # needed for snake animation
    time.sleep(0.2) # needed for snake animation
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15: # http://docs.python.org/3.10/library/turtle.html#turtle.distance
        # print("yum")
        food.refresh()
        scoreboard.update_score()
        snake.extend()
    # Detect collision with wall - finish game
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over_sign()
    # Detect collision with itself - finish game
    # if heads collides with any square in tail - finish game
    for square in snake.segments[1:]:
        # if square == snake.head: # to prevent game over as snake head is always within 10 distance to itself
        #     pass
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over_sign()

# print(starting_positions) # DEBUG
# print(segments) # DEBUG
screen.exitonclick()