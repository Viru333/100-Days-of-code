import random
import os

def clear():
    os.system('cls')

import art
logo = art.logo
vs = art.vs

import game_data

data = game_data.data

def get_random_option(data):
    i = random.randint(0,len(data)-1)
    return data[i]

def compare(option_1, option_2):

    if option_1["follower_count"] > option_2["follower_count"]:
        return "A"
    elif option_1["follower_count"] < option_2["follower_count"]:
        return "B"
    else:
        return "0"

def play_game():
    lose = False
    score = 0
    option_1 = get_random_option(data)
    option_2 = get_random_option(data)
    print(logo)
    while not lose:
        
        print(f"Compare A: {option_1["name"]}, a {option_1["description"]}, from {option_1["country"]}.")

        print(vs)

        print(f"Against B: {option_2["name"]}, a {option_2["description"]}, from {option_2["country"]}.")

        predicted = input("Who has more followers? Type 'A' or 'B' and for equal followers count type 0:")

        actual = compare(option_1, option_2)

        if actual == predicted:
            score += 1
            option_1 = option_2
            option_2 = get_random_option(data)
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")

        else:
            clear()
            print(f"You're wrong! Your Final score is: {score}.")
            lose = True

play_game()