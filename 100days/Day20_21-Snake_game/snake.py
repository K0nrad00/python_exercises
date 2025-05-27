from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def move(self):
        for square_num in range(len(self.segments) - 1, 0,
                                -1):  # moving squares from last one in the list to first one, so they follow each other
            new_x = self.segments[square_num -1].xcor() # second to last square, no 2
            new_y = self.segments[square_num - 1].ycor()
            self.segments[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def add_square(self, position): # when snake 'collides'/eats food
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def extend(self):
        self.add_square(self.segments[-1].position()) # adding last square



