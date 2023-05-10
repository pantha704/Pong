from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.wall_bounce()
    if ball.distance(r_paddle) <= 30 or ball.distance(l_paddle) <= 30:
        ball.paddle_bounce()

    if ball.xcor() > 400:
        ball.reset_pos()
        score.le_score()
    if ball.xcor() < -400:
        ball.reset_pos()
        score.ri_score()

screen.exitonclick()
