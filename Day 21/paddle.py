from turtle import Turtle, Screen
class Paddle:
    def __init__(self):
        self.paddles=[]
        for self.Paddles in range(1,3):
            self.Paddles=Turtle(shape="square")
            self.Paddles.penup()
            self.Paddles.color("white")
            self.Paddles.shapesize(5, 1)
            self.paddles.append(self.Paddles)
        self.first_p=self.paddles[0]
        self.second_p=self.paddles[1]
    def set_paddles(self):
        self.first_p.goto(-390,0)
        self.second_p.goto(380,0)
    def move_paddles(self):
        if self.first_p.ycor() > 250:
            self.first_p.goto(self.first_p.xcor(), 250)
        if self.first_p.ycor() < -250:
            self.first_p.goto(self.first_p.xcor(), -250)
        if self.second_p.ycor() > 250:
            self.second_p.goto(self.second_p.xcor(), 250)
        if self.second_p.ycor() < -250:
            self.second_p.goto(self.second_p.xcor(), -250)
# if paddle.ycor() > 250:
#     paddle.goto(paddle.xcor(), 250)
# if paddle.ycor() < -250:
#     paddle.goto(paddle.xcor(), -250)          