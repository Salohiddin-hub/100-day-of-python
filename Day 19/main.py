from turtle import Turtle, Screen
tim=Turtle()
screen=Screen()

def tim_forward():
    tim.forward(10)
def tim_backward():
    tim.backward(10)
def tim_right():
    tim.right(10)
def tim_left():
    tim.left(10)
def tim_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.penwdown()

screen.listen()
screen.onkey(key="w", fun=tim_forward)
screen.onkey(key="s", fun=tim_backward)
screen.onkey(key="a", fun=tim_left)
screen.onkey(key="d", fun=tim_right)
screen.onkey(key="c", fun=tim_clear)
screen.exitonclick()
