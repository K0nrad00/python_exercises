from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True
coffe_maker = CoffeeMaker()
items = Menu().get_items()
money_machine = MoneyMachine()
menu = Menu()
# print(menu.get_items()) # DEBUG
# menu_item = MenuItem # not needed

while machine_is_on:
    choice = input(f"What would you like? {items}: ")
    if choice == "off":
        print("Powering down")
        machine_is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        chosen_drink = menu.find_drink(choice)
        drink_name, drink_cost = chosen_drink.name, chosen_drink.cost # drink_name not used can be removed hereś
        print(chosen_drink) # DEBUG
        # print(f"Menu item name, cost: {drink_name}, {drink_cost}") # DEBUG
        if coffe_maker.is_resource_sufficient(chosen_drink):
            # prompt to insert coins
            # money_machine.process_coins() # NOT NEEDED, its used by make_payment
            if money_machine.make_payment(cost=drink_cost):
            # If the transaction is successful and there are enough resources to make the drink the user selected,
            # then the ingredients to make the drink should be deducted from the coffee machine resources.
                coffe_maker.make_coffee(chosen_drink)
