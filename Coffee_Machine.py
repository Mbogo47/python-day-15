from Coffee_Machine import MENU, resources

on = True
profit = 0


def money():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many pennies?: ")) * 0.01
    total = int(input("How many nickels?: ")) * 0.05
    total = int(input("How many dimes?: ")) * 0.1
    total = int(input("How many quarters?: ")) * 0.25
    return total


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")


def is_resource_sufficient(order_ingredient):
    """Returns True when order can be made,False if ingredients are not enough"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item} ")
            return False
        return True


def is_transaction_successful(money_received, drink_cost):
    """Returns True when payment is accepted or false if money is not enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money,Money refunded")
        return False


while on:
    coffee_type = input("What would you like?(espresso/latte/cappuccino):")
    if coffee_type == "off":
        on = False
    elif coffee_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money:$ {profit}")
    else:
        coffee = MENU[coffee_type]
        if is_resource_sufficient(coffee["ingredients"]):
            payment = money()
            if is_transaction_successful(payment, coffee['cost']):
                make_coffee(coffee_type,coffee['ingredients'])
