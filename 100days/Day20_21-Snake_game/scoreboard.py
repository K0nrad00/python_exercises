from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("blank")
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over_sign(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

