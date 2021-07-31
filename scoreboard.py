from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.data = open("data.txt", mode='r')
        self.score = 0
        self.high_score = int(self.data.read())
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)
        self.data.close()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", move=False, align="center", font=('Arial', 15))

    def inc_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.data = open("data.txt", mode='w')
            self.data.write(str(self.score))
            self.high_score = self.score
            self.data.close()
        self.score = 0
        self.write_score()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game over", align='center', font=('Arial', 15))
