# <--- TIP CALCULATORR PROJECT -- DAY 2 --->

print("Welcome to the Tip calculator!")
bill = float(input("What was your total bill? $"))

tip = float(input("How much tip would you like to give? 10, 12, or 15? "))

person = float(input("how many people to split the bill? "))

per_person_bill = bill/person
per_person_tip = ((bill*tip)/100)/person
per_person_total_bill = per_person_bill + per_person_tip
per_person_total_bill = round(per_person_total_bill,2)
per_person_total_bill = "{:.2f}".format(per_person_total_bill)
print(f"Each person should pay: ${per_person_total_bill}")