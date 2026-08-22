from turtle import Turtle, Screen
screen=Screen()

class Paddle:
    def __init__(self):

        self.paddles=[]

        for self.Paddles in range(1,3):
            self.Paddles=Turtle(shape="square")
            self.Paddles.color("white")
            self.Paddles.shapesize(5, 1)
            self.Paddles.penup()
            self.paddles.append(self.Paddles)

        self.first_p=self.paddles[0]
        self.second_p=self.paddles[1]
    def set_paddles(self):
        self.first_p.goto(-350,0)
        self.second_p.goto(350,0)

    def go_up_first(self):
        self.first_p.sety(self.first_p.ycor()+20)
        
    def go_down_first(self):
        self.first_p.sety(self.first_p.ycor()-20)

    def go_up_second(self):
        self.second_p.sety(self.second_p.ycor()+20)
        
    def go_down_second(self):
        self.second_p.sety(self.second_p.ycor()-20)

        