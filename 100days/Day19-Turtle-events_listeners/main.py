from turtle import Turtle, Screen

tim = Turtle()
print(tim)
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(45)
    move_forwards()

def move_clockwise():
    tim.right(45)
    move_forwards()

# W - forwards
screen.listen()
screen.onkey(key="W".lower(), fun=move_forwards) # higher order function

# S - backwards
screen.onkey(key="S".lower(), fun=move_backwards)

# A - Counter clockwise
screen.onkey(key="A".lower(), fun=move_counter_clockwise)

# D - clockwise
screen.onkey(key="D".lower(), fun=move_clockwise)

# C - clear
screen.onkey(key="C".lower(), fun=tim.reset)


screen.exitonclick()