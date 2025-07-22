#Module to clear screen
import os
def clear(): #Fuction using os module to clear screen
    os.system('cls')

from art import logo #printing logo 
print(logo)

print("Welcome to the secret auction program.\n")

auction_details = {} #List of auction details containing bidder's name and his bid

should_continue = True
max_bid = 0

while should_continue:
    bidder_name = input("What is your name? ")
    bidder_bid = int(input("What's your bid $"))
    
    auction_details[bidder_name] = bidder_bid
    
    next_bidder = input("Are there any other bidders? 'yes' or 'no'. ").lower()

    if next_bidder == "no":
        should_continue = False
    else:
        clear()
ans = ""
for key in auction_details:
    if auction_details[key] > max_bid:
        ans = key
        max_bid=auction_details[key]
    
clear()
print(f"The winner is {ans} with a bid of ${auction_details[ans]}.\n")
# print(auction_details[0])


