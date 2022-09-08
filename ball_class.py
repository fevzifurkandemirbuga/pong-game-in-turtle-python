from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed(0)
        self.create_strips()
        self.goto(0, 0)
        self.shape("circle")
        self.speed(1)
        self.setheading(30)
    
    def create_strips(self):
        for i in range(290, -290, -25):
            self.goto(-5, i)
            self.begin_fill()
            self.fillcolor("white")
            self.setheading(0)
            for j in range(3):
                self.forward(10)
                self.right(90)
            self.forward(10)
            self.end_fill()
        