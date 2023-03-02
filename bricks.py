from turtle import Turtle
import random

COLORS = ["dark violet", "magenta", "red", "dark orange", "yellow",
          "lime", "medium spring green", "dodger blue", "blue"]
WEIGHTS = [1, 1, 2, 1, 3, 2, 1, 1, 4, 1, 2, 1, 1, 1, 3, 2, 1, 4, 1, 1, 2, 3]


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(COLORS))
        self.goto(x=x_cor, y=y_cor)
        self.quantity = random.choice(WEIGHTS)
        self.left_side = self.xcor() - 30
        self.right_side = self.xcor() + 30
        self.top_side = self.ycor() + 15
        self.bottom_side = self.ycor() - 15


class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = -240
        self.bricks = []
        self.create_all_lines()

    def create_line(self, y_cor):
        for i in range(-570, 570, 63):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)

    def create_all_lines(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_line(i)
