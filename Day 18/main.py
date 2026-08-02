# import colorgram
# colors=colorgram.extract('paint.jpg', 100)
# rgb_color=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_colors=(r, g, b)
#     rgb_color.append(new_colors)
# print(rgb_color)

color_list=[(253, 251, 247), (253, 248, 251), (235, 251, 243), (198, 13, 32), (248, 236, 26), (40, 77, 188), (227, 159, 51), (40, 217, 70), (238, 227, 5), (242, 246, 252), (29, 39, 154), (212, 75, 15), (17, 153, 17), (222, 21, 119), (194, 15, 11), (240, 38, 162), (68, 10, 31), (221, 141, 203), (60, 15, 9), (11, 97, 63), (55, 209, 230), (218, 159, 11), (17, 19, 49), (235, 158, 214), (77, 212, 165), (84, 76, 209), (11, 227, 238), (106, 230, 194), (217, 87, 50), (6, 67, 42), (69, 231, 239), (174, 180, 228), (233, 171, 165), (250, 7, 56), (4, 247, 221), (9, 80, 109), (22, 54, 238), (72, 63, 54)]
from turtle import Turtle, Screen
import random
t=Turtle()
s=Screen()
s.colormode(255)
t.hideturtle()
t.speed("fastest")
width=-135
height=-135
t.penup()  
for row in range(10):
    angle= height +(row * 20)
    t.goto(width, angle)
    height+=10
    for _ in range(10):
        t.dot(15, random.choice(color_list))
        t.penup()
        t.forward(30)       
s.exitonclick()