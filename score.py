from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=('Courier', 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=('Courier', 80, "normal"))

    def le_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def ri_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
