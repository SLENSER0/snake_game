from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0,275)

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 15))
    def inc_score(self):
        self.score += 1
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game over" , align='center', font=('Arial', 15))


