from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

def start_cofee_machine():
    is_on = True
    print(logo)
    money_machine = MoneyMachine()
    menu = Menu()
    coffee_maker = CoffeeMaker()
    while(is_on):
        order = input(f"What would you like to have? {menu.get_items()}: ")

        if order == "report":
            coffee_maker.report()

        elif order == "off":
            is_on = False

        elif order == "profit":
            money_machine.report()

        else:
            drink = menu.find_drink(order)
            if drink:
                sufficient = coffee_maker.is_resource_sufficient(drink)
                if sufficient:
                    transaction = money_machine.make_payment(drink.cost)
                    if transaction:
                        coffee_maker.make_coffee(drink)

start_cofee_machine()



