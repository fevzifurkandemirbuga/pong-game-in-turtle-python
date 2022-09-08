from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write(f"0     0", align="center", font=("arial", 20, "normal"))
    
    def update(self, score1, score2):
        self.clear()
        self.goto(0, 250)
        self.write(f"{score1}     {score2}", align="center", font=("arial", 20, "normal"))
