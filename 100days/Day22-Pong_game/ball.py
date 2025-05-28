from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        # self.goto(self.xcor() + self.bounce_x(), self.xcor() + self.bounce_y())
        # y_cor += movement

    def bounce_y(self):
        self.y_move *= -1 # reverse ycor

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.home()
        self.x_move *= -1
        self.y_move *= -1
        self.move_ball()
