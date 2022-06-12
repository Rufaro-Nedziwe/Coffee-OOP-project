# from turtle import Turtle, Screen
# rue=Turtle()
# print(rue)
# my_screen= Screen()
# print(my_screen.canvheight)
# rue.shape("triangle")
# rue.color("red")
# rue.forward(100)
# rue.right(40)
# rue.left(56)
# my_screen.exitonclick()

import prettytable
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)
