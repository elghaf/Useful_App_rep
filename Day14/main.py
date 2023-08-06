# TODO : chech the menu 
MENU = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "lette": {
        "ingredients":{
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough water {item}.")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    """
    return True when the payment is accepted, or
    false if money is insufficient.

    """
    if money_received >= drink_cost:
        return True
    else:
        print("Sorry thats not enough money.")
        return False


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    Total = int(input("how many quarters?")) * 0.25
    
    return Total


while is_on:
    choice = input("what would you like ? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit : {profit} dollars")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = ''
