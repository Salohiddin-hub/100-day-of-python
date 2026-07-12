# from turtle import Turtle, Screen
# timmy=Turtle()
# print(timmy)
# my_screen=Screen()
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# table.field_names=["City names", "Area", "Population"]
# table.add_row(["Andijan", "1234", "1_411_500"])
# table.add_row(["Fergana", "1123", "1_100_323"])
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align="c"
table.valign="b"
print(table)
