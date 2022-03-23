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


def check_resources(coffee,resources):

    for item in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        else:
            return True


def process_coins():
    amount = {
        "quarters": {
            "cost": 0.25
        },
        "dimes": {
            "cost": 0.10
        },
        "nickles": {
            "cost": 0.05
        },
        "pennies": {
            "cost": 0.01
        }
    }

    total_amount = 0
    for key in amount:
        amount[key]["quantity"] = int(input(f"How many {key} ?: "))
        total_amount = total_amount + amount[key]["quantity"] * amount[key]["cost"]
    return total_amount


money = 0
machine_on = True
while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 1. Print report of all coffee machine resources
    if order == "report":
        print(f"Water: {resources['water']}ml"
              f"\nMilk: {resources['milk']}ml"
              f"\nCoffee: {resources['coffee']}g"
              f"\nMoney: ${money}")
    elif order == "off":
        machine_on = False
    else:
        # TODO: 2. Check resources sufficient
        # TODO: 3: Process coins
        if check_resources(order, resources) == True:
            total_amount = process_coins()
            # TODO: 4. Check transaction successful

            if total_amount >= MENU[order]['cost']:
                print(f"Here is ${MENU[order]['cost']} in charge.")
                money += MENU[order]['cost']
                print("Here is your latte ☕️. Enjoy!")
                for item in MENU[order]['ingredients']:
                    resources[item] -= MENU[order]["ingredients"][item]
            else:
                print("Sorry that's not enough money. Money refunded.")









