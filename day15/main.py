MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money_made = 0
while True:
    type_of_coffee = input("What would you like? (espresso: $1.5/latte: $2.5/cappuccino: $3.0): ")
    Coffee_True = False
    for key in MENU:
        if key == type_of_coffee:
            Coffee_True = True

    if type_of_coffee == 'resources':
        print(f"{resources} and money earned: {money_made}")

    elif type_of_coffee == 'refill':
        for key in resources:
            resources[key] += int(input(f'refill of {key} (0-1000): '))

    elif Coffee_True:
        print('Please insert coins.')
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes   ?: "))
        nickles = int(input("How many nickles ?: "))
        pennies = int(input("How many pennies ?: "))
        coffee_cost = MENU[type_of_coffee]['cost']
        total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        if total_money < coffee_cost:
            print("Sorry that's not enough money. Money refunded")
        else:
            refund_money = total_money - coffee_cost
            money_made += coffee_cost
            print(f"Your coffee will be ready shortly. Take the change {round(refund_money, 2)}")
            refill = False
            for key in resources:
                if resources[key] - MENU[type_of_coffee]['ingredients'][key] < 0:
                    print(f"Insufficient {key}. Please refill the machine")
                    refill = True
            if not refill:
                for key in resources:
                    resources[key] = resources[key] - MENU[type_of_coffee]['ingredients'][key]
                print(f'"Here is your {type_of_coffee}. Enjoy!".')

    else:
        print("Incorrect input")

