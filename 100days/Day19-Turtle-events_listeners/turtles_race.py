import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="MAKE a BET", prompt="Enter turtle color: ")
colors = ["red", "orange", "black", "green", "blue", "purple"]
turtles = []

y_axis = -100
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    new_turtle.speed("fast")
    y_axis += 40
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            # print(turtle.color())
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won, winning turtle is {winning_color}")
            else:
                print(f"You've lost, winning turtle is {winning_color}")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
