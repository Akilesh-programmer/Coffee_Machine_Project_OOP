from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    choices = menu.get_items()
    user_choice = input(f"What would you like? ({choices}):  ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)