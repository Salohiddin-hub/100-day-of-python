from turtle import Screen
import time
from snake import Snake

snake=Snake()
screen=Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.tracer(0)


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()