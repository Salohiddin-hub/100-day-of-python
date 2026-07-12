
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menyu=Menu()
Coffee_maker=CoffeeMaker()
Money_machine=MoneyMachine()
is_on=True
while is_on == True:
    wish=input("What would you like to drink? espresso/latte/cappuccino: " )
    if wish == "off":
        print("Turning off the machine.")
        exit()
    if wish == "report":
        Money_machine.report()
        Coffee_maker.report()
        continue
    drink_order = menyu.find_drink(wish)
    # Use that object for your checks and coffee making
    if drink_order is not None:
        # Check resources first using the object
        if Coffee_maker.is_resource_sufficient(drink_order):
            # Process payment using the object's cost attribute
            if Money_machine.make_payment(drink_order.cost):
                # Make the coffee
                Coffee_maker.make_coffee(drink_order)
