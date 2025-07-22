print(r'''
################################################################
----------------------------------------------------------------
****************************************************************
||                    ____...------------...____              ||
||               _.-"` /o/__ ____ __ __  __ \o\_`"-._         ||
||             .'     / /                    \ \     '.       ||
||             |=====/o/======================\o\=====|       ||
||             |____/_/________..____..________\_\____|       ||
||             /   _/ \_     <_o#\__/#o_>     _/ \_   \       ||
||             \_________\####/_________/                     ||
||              |===\!/========================\!/===|        ||
||              |   |=|          .---.         |=|   |        ||
||              |===|o|=========/     \========|o|===|        ||
||              |   | |         \() ()/        | |   |        ||
||              |===|o|======{'-.) A (.-'}=====|o|===|        ||
||              | __/ \__     '-.\uuu/.-'    __/ \__ |        ||
||              |==== .'.'^'.'.====|                          ||
||          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|        ||
||              `""""-""""""""""""""""""""""""""-""""`        ||
################################################################
----------------------------------------------------------------
****************************************************************
      ''')
print("Welcome to Tresure Island\n")
print("Your mission is to find the treasure\n")

print("Look there is a crossroad.\n")
go = input("Where did you want to go? Left or Right? ")
go = go.lower()
if go != "left":
    print("Oops! You fall into a hole\n---GAME OVER---\n")
else:
    action = input("Look there is a river.What do you want to do? Swim or Wait? ")
    action = action.lower()
    if action != "wait":
        print("Oh no!! You got attacked by trout\n---GAME OVER---\n")
    else:
        door = input("Look there are coloured doors.which color door you want to open? Red, Blue or Yellow? ")
        door = door.lower()

        if door != "yellow" and door == "red":
            print("Oh hell!! Your were burned by fire\n---GAME OVER---\n")
        elif door != "yelow" and door == "blue":
            print("Horrible!! you were eaten by the beasts\n---GAME OVER---\n")
        elif door != "yellow":
            print("---GAME OVER---\n")
        else:
            print("----------- Hurray !! You win! ------------")

