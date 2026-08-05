from turtle import Turtle
ALIGNMENT = "center"
FONT= ('Times New Roman', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 279) 
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)
    def increase_score(self):
        self.score+=1
        self.update_score()    