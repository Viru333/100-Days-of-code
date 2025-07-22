print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age >= 45 and age <= 55:
        print("!!Hurray, You can ride roller coaster for free!!\n----------Enjoy the ride----------")
    elif age < 12:
        bill = 5            #nested if else
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you Want a photo of you enjoying ride? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry,You cannot ride the rollercoaster!")