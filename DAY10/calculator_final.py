#calculator
from calc_art import logo
import os
def clear():
    os.system('cls')
#Add
def add(n1, n2):
    return n1+n2

#Subtract
def subtract(n1, n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1, n2):
    return n1/n2

#Dictionary for saving info about operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    calculation_finished = False

    while not calculation_finished:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'exit' to finish calculation. ")
        if should_continue == 'n':
            calculation_finished = True
            clear()
            calculator()
        elif should_continue == 'exit':
            calculation_finished = True
            clear()
        else:
            num1 = answer

calculator()