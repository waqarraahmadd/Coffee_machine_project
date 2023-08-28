MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

MONEY = {
    "quarters": "0.25",
    "dimes": "0.10",
    "nickles": "0.05",
    "pennies": "0.01"
}



def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is enough {item}")
            return False
    return True


def user_money():
    """Returns the total calculated from coins inserted."""
    print("Please inset coins.")
    total = float(input("how many quarters?: ")) * 0.25
    total += float(input("how many dimes?: ")) * 0.10
    total += float(input("how many nickles?: ")) * 0.05
    total += float(input("how many pennies?: ")) * 0.01
    return total


def update_resources(order_ingredients, drink_name):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name.capitalize()}, enjoy!")


def transaction_successful(user_payment, cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if cost > user_payment:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif user_payment > cost:
        change = round((user_payment - cost), 2)
        print(f"Here is ${change} in your change")
        global profit
        profit += cost
        return True


def report(current_resources,current_profit):
    print(f"Water: {current_resources['water']} ml")
    print(f"Milk: {current_resources['milk']} ml")
    print(f"Coffee: {current_resources['coffee']} g")
    print(f"Profit: ${current_profit}")


profit = 0
coffee_machine_is_on = True

while coffee_machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        report(resources,profit)
    elif choice == "off":
        print("Shutting down.")
        coffee_machine_is_on = False
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = user_money()
            if transaction_successful(payment, drink['cost']):
                update_resources(drink['ingredients'], choice)
