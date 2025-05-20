MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Turn off the Coffee Machine by entering “off” to the prompt.
is_machine_on = True

# check if ingredients_dict for chosen drink are sufficient
def calculate_resources(user_drink, ingredients_dict):
    current_resources = {}
    for res in ingredients_dict:
        if res in user_drink["ingredients"]:
            current_resources[res] = ingredients_dict[res] - user_drink["ingredients"][res]
        else:
            current_resources[res] = ingredients_dict[res]
    return current_resources


def is_resource_sufficient(user_drink: dict) -> bool:
    # This does not provide all missing ingredients, just 1st that prevents from making the drink
    for item in user_drink:
        if user_drink[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True

def process_coins(quarters_amount, dimes_amount, nickles_amount, pennies_amount):
    total_given = (quarters_amount * 0.25) + (dimes_amount * 0.1) + (nickles_amount * 0.05) + (pennies_amount * 0.01)
    return total_given

money_in_machine = 0
calculated_resources = {}
user_coins = 0

while is_machine_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            chosen_drink_ingredients = MENU[user_choice]
            # print("Chosen drink", chosen_drink_ingredients)  # DEBUG
            chosen_drink_cost = MENU[user_choice]['cost']
            # print("Drink cost", chosen_drink_cost)  # DEBUG
            # only ask for user_coins if there's enough resources
            if is_resource_sufficient(chosen_drink_ingredients["ingredients"]):
                quarters = float(input("Please insert the coins. \nHow many quarters?: "))  # 25c -> 0.25
                dimes = float(input("How many dimes?: "))  # 10c -> 0.1
                nickles = float(input("How many nickles: "))  # 5c -> 0.05
                pennies = float(input("How many pennies: "))  # 1c -> 0.01
                user_coins = process_coins(quarters, dimes, nickles, pennies)
                # Check that the user has inserted enough money to purchase the drink they selected.
                if user_coins < chosen_drink_cost:
                    print(f"Sorry that's not enough coins. Money refunded: ${user_coins}.")
                else:
                    money_in_machine += chosen_drink_cost
                    user_change = round(user_coins - chosen_drink_cost, 2)
                    print(f"Here's your change: ${user_change}, Enjoy your drink")
                    # update the resources each time
                    calculated_resources = calculate_resources(chosen_drink_ingredients, resources)
                    resources = calculate_resources(chosen_drink_ingredients,
                                                    resources)  # udpating resource dict with calculate_resources for next run
        elif user_choice == "off":
            print("Powering off..")
            is_machine_on = False
        elif user_choice == "report":
            for resource in resources:
                print(resource.title(), resources[resource])
            print(f"Money: ${money_in_machine}", )
        else:
            print("I don't know what that is, try again")

