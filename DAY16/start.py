# from turtle import Turtle, Screen
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("circle")
# timmy.color("cyan1")
# timmy.fd(100)
# timmy.right(90)
# timmy.fd(100)
# timmy.right(90)
# timmy.fd(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Charlizard","Blastoise", "Veinasauras"])
table.add_column("Type", ["Fire", "Water", "Grass"])
table.align = "l"
print(table)
