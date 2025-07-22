import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock,paper,scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")
player_input = int(input())
print(f"You Chose:{game[player_input]}")
print("\n")

computer_chose = random.randint(0,2)
print(f"Computer Chose:{game[computer_chose]}")
print("\n")

if player_input == computer_chose:
    print("It's a Draw\n")
elif player_input == 0:
    if computer_chose == 1:
        print("You lose\n")
    else:
        print("You Win\n")
elif player_input == 1:
    if computer_chose == 0:
        print("You Win\n")
    else:
        print("You lose\n")
elif player_input == 2:
    if computer_chose == 0:
        print("You lose\n")
    else:
        print("You Win\n")