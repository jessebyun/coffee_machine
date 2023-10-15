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

profit = 0.00


# TODO: 4. Check resources sufficient
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 5. Process coins
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# TODO: 6. Check transaction successful?
def is_transaction_successful(payment_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if payment_received >= drink_cost:
        change = round(payment_received - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7. Make coffee
def make_coffee(drink, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")


is_on = True

while is_on:
    # TODO: 1. prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    choice = input("\tWhat would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    if choice == "off":
        is_on = False

    # TODO: 3. Print report
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
