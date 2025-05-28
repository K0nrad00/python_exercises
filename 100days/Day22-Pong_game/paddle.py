from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5.0, stretch_len=1.0)
        self.movement = 20
        # self.x_pos = x_pos
        # self.y_pos = y_pos
        self.goto(position)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor()+self.movement)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor()-self.movement)

