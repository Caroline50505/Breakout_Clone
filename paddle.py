from turtle import Turtle

TRAVEL_DIS = 100


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("deep sky blue")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-280)

    def move_left(self):
        self.bk(TRAVEL_DIS)

    def move_right(self):
        self.fd(TRAVEL_DIS)
