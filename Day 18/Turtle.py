
from turtle import Turtle, Screen
import random
timmy=Turtle()

# for _ in range(15):
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()


# def draw_shape(num_sides):    
#     angle=360/num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
# for number in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(number)

screen=Screen()
screen.colormode(255)
def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    random_color=(r, g, b)
    return random_color
        
# timmy.pensize(15)
# timmy.speed("fastest")
# directions=[0, 90, 180, 270]
# for _ in range(200):
#     timmy.forward(30)
#     timmy.color(random_color())
#     timmy.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
    timmy.speed("slow")
    for _ in range(int(360/size_of_gap)):
        timmy.setheading(timmy.heading()+size_of_gap)
        timmy.color(random_color())
        timmy.circle(100)
draw_spirograph(5)


# from prettytable import PrettyTable
# table = PrettyTable()
# # table.field_names=["City names", "Area", "Population"]
# # table.add_row(["Andijan", "1234", "1_411_500"])
# # table.add_row(["Fergana", "1123", "1_100_323"])
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align="c"
# table.valign="b"
# print(table)

screen.exitonclick()
# turtle colors - (TK colors) website that change color