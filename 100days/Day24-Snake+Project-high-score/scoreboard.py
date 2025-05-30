from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt") as f:
            self.highest_score = int(f.readline())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score :{self.highest_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        """set score to highest score if it's higher than current highest score"""
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", "w") as f:
                f.write(str(self.highest_score))
        self.score = 0 # reset score to 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
