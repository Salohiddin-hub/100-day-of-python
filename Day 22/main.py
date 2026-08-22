from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

paddle=Paddle()

turtle=Turtle()
ball=Ball()
score=Scoreboard()

screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle.set_paddles()
screen.listen()
screen.onkey(paddle.go_up_first, "w")
screen.onkey(paddle.go_down_first, "s")
screen.onkey(paddle.go_up_second, "Up")
screen.onkey(paddle.go_down_second, "Down")



game_is_on=True
while game_is_on:
    time.sleep(0.1)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle.second_p) < 50 and ball.xcor()>320 or ball.distance(paddle.first_p) < 50 and ball.xcor()<-320:
        ball.bounce_x()
       
    # Detect R paddle misses
    if ball.xcor()>350:
        ball.reset_postion()
        score.l_point()
    # Detect L paddle misses
    if ball.xcor()<-350:
        ball.reset_postion()
        score.r_point()
    
        
    screen.update()

screen.exitonclick()