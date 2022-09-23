from turtle import Screen, Turtle
from Paddle import Paddle
from ball import Ball
from scor import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800 ,height=900)
screen.title("Pong")
screen.tracer(0)


screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scor_board = Score()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
ball = Ball()
game_is_on = True
sleep_time = 0.1
while game_is_on:
    if sleep_time - 0.0001 > 0:
        sleep_time -= 0.0001
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    if ball.ycor() >= 380 or ball.ycor() < -380:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330\
            or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.x_move *= -1
    if ball.xcor() > 350:
        scor_board.l_point()
        scor_board.update_scoreboard()
        ball.reset_position()
    if ball.xcor() < -350:
        scor_board.r_point()
        scor_board.update_scoreboard()
        ball.reset_position()

screen.exitonclick()