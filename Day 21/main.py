from turtle import Turtle, Screen
from paddle import Paddle
paddle=Paddle()
turtle=Turtle()
screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
while True:
    paddle.move_paddles()









screen.exitonclick()