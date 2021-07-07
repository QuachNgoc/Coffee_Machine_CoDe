from MENU import MENU
from MENU import resources
from art import logo
from time import sleep

print(logo)


def water(name):
    return MENU[name]['ingredients']['water']


def coffee(name):
    return MENU[name]['ingredients']['coffee']


def milk(name):
    return MENU[name]['ingredients']['milk']


def cost_to_pay(name):
    return MENU[name]['cost']


def check(a, b):
    return a > b


def reduce(a, b):
    return a - b

# TODO: 2. Serving the customer
def new_customer():
    global choice
    water_in_machine = resources['water']
    milk_in_machine = resources['milk']
    coffee_in_machine = resources['coffee']
    cost = 0

    serving = True
    while serving:
    # TODO 3: 3. Let the customer choose drink
        choice = input("\nWhat would you like? ('espresso','latte', 'cappuccino') or "
                       "'report' to show the resources or "
                       "'ok' to finish choosing : ")
        print("Please waiting...")
        sleep(2)
        # print the resource in this machine
        if choice == 'report':
            print(
                f"\nThis machine has WATER: {water_in_machine} ml, MILK: {milk_in_machine} ml, COFFEE: {coffee_in_machine} g, MONEY TO PAY: {cost}$")
            print("--MENU PRICES--")
            print(f"Espresso price: {MENU['espresso']['cost']} $")
            print(f"Latte price: {MENU['latte']['cost']} $")
            print(f"Cappuccino price: {MENU['cappuccino']['cost']}$")

        elif choice != 'report' and choice != 'ok':
            #TODO: Check the resource in the machine
            if not check(water_in_machine, water(choice)): # if water in the machine is not enough to make the coffee
                print(f'Sorry, not enough water to make {choice}')
            else:
                water_in_machine = reduce(water_in_machine, water(choice))
            if not check(milk_in_machine, milk(choice)): # if milk in the machine is not enough to make the coffee
                print(f'Sorry, not enough milk to make {choice}')
            else:
                milk_in_machine = reduce(milk_in_machine, milk(choice))
            if not check(coffee_in_machine, coffee(choice)): # if coffee in the machine is not enough to make the coffee
                print(f'Sorry, not enough coffee to make {choice}')
            else:
                coffee_in_machine = reduce(coffee_in_machine, coffee(choice))
            cost += cost_to_pay(choice)
            current_drink = choice
            print(f"\nYour {choice} is ready! ☕☕")

        elif choice == 'ok':
            print(f'Your bills is {cost}$\n')
            serving = False

    # TODO: 4. Customer's Payment
    if cost != 0: # if the customer don't want to pay(cost = 0) , stop the machine
        paying = True
        while paying:
            print("Please waiting...")
            sleep(2)
            print("\nPlease insert coin: ")
            quarters = int(input('Quarters: '))
            dimes = int(input('Dimes: '))
            nickles = int(input('Nickles: '))
            pennies = int(input('Pennies: '))

            paid = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

            if check(cost, paid):
                print(f"Your money is {paid}.You don't have enough money. Money refund 💸💸 ")
                stop_paying = input("Do you want to keep paying bills? 'y' or 'n': ")
                if stop_paying == 'n':
                    paying = False
            else:
                print(f"Your change: { round(reduce(paid, cost), 2) }$")
                paying = False

        print("Please waiting...")
        sleep(2)
        print(f"Here is your {current_drink} ☕☕. Enjoy~❤")
    else:
        print("\nSee you later!")


# TODO: 1.Turn on the machine
begin = input("Turn on the machine? 'on' or 'off': ")
while begin == 'on':
    print("\nPlease wait while the coffee machine is refilling...")
    sleep(2)
    customer = input("New customer? 'y' or 'n': ")
    if customer == 'y':
        new_customer()
    else:
        begin = input("Turn on the machine? 'on' or 'off': ")
