#calculator

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
    num1 = int(input("What's the first number?: "))
    calculation_finished = False

    while not calculation_finished:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ")

        num2 = int(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ")
        if should_continue == 'n':
            calculation_finished = True
            calculator()
        else:
            num1 = answer

calculator()