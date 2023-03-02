import turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from ui import UI
from scoreboard import Scoreboard
import time

window = turtle.Screen()
window.setup(width=1200, height=600)
window.bgcolor("black")
window.title("Breakout")
window.tracer(0)

ui = UI()
ui.header()

score = Scoreboard(lives=5)
paddle = Paddle()
ball = Ball()
bricks = Bricks()

game_paused = False
game_running = True


def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True


window.listen()
window.onkey(paddle.move_left, "a")
window.onkey(paddle.move_right, "d")
window.onkey(pause_game, "space")


def check_walls():
    global ball, score, game_running, ui
    if ball.xcor() < -580 or ball.xcor() > 580:
        ball.bounce(x_bounce=True, y_bounce=False)
        return
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        return
    if ball.ycor() < -280:
        ball.reset()
        score.decrease_lives()
        if score.lives == 0:
            score.reset()
            game_running = False
            ui.game_over(win=False)
            return
        ui.change_color()
        return


def check_paddles():
    global ball, paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()
    if ball.distance(paddle) < 110 and ball.ycor() < -250:
        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        else:
            if ball_x < paddle_x or ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)


def check_bricks():
    global ball, score, bricks
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            score.increase_score()
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)
            if ball.xcor() > brick.right_side or ball.xcor() < brick.left_side:
                ball.bounce(x_bounce=True, y_bounce=False)
                return
            elif ball.ycor() < brick.bottom_side or ball.ycor() > brick.top_side:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


while game_running:
    if not game_paused:
        window.update()
        time.sleep(0.01)
        ball.move()

        check_walls()
        check_paddles()
        check_bricks()

        if len(bricks.bricks) == 0:
            ui.game_over(win=True)
            break
    else:
        ui.paused_status()

turtle.mainloop()
