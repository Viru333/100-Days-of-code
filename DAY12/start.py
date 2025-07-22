# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

# # print(potion_strength)

# #Global Scope

# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()




#There is no Block space in Python
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0] #Names created inside if while for orany block that has indentation and colon can be accesed in its local space

# print(new_enemy)


#Modify Global Variable
# enemies = 1

# def increase_enemies():
#     # global enemies
#     # enemies = 2
#     print(f"enemies inside function: {enemies}")
#     return enemies+1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")



#Global Constant

# pi = 3.1415
# URL = "https://www.google.com"


i = 50

def inc():
    i = 100

    return i

ans = inc()

print(ans)