from turtle import Turtle
from paddle import Paddle
from bricks import Bricks
from scoreboard import Scoreboard

TRAVEL_DIST = 10
paddle = Paddle()
bricks = Bricks()
score = Scoreboard()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("alice blue")
        self.penup()
        self.x_move_dist = TRAVEL_DIST
        self.y_move_dist = TRAVEL_DIST
        self.reset()

    def move(self):
        new_x = self.xcor() + self.x_move_dist
        new_y = self.ycor() + self.y_move_dist
        self.goto(new_x, new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move_dist *= -1
        if y_bounce:
            self.y_move_dist *= -1

    def reset(self):
        self.goto(x=0, y=-240)
        self.y_move_dist = 10


