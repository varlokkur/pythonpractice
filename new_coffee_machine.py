# Only input available is the console; should limit the number of options.
# Machine could have a 'state' attribute that gets modified, according to selected/entered input
# Program could check this state and offer appropriate options


class CoffeeMachine:
    water = None
    milk = None
    beans = None
    disposable_cups = None
    money = None
    state = None

    def __init__(self, water, milk, beans, disposable_cups, money, state):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.disposable_cups = disposable_cups
        self.money = money
        self.state = state

    def __str__(self):
        return f"""
        The coffee machine has:
        {self.water} ml of water
        {self.milk} ml of milk
        {self.beans} g of coffee beans
        {self.disposable_cups} disposable cups
        ${self.money} money
"""

# side project / enhancement -- fix this up later?
# class Coffee:
#     coffee_menu = []
#
#     def __init__(self, water, milk, beans, money):
#         self.water = None
#         self.milk = None
#         self.beans = None
#         self.disposable_cups = 1
#         self.money = None
#         Coffee.coffee_menu.append(self)
#
#
# espresso = Coffee(water=250, milk=0, beans=16, money=4)
# latte = Coffee(water=350, milk=75, beans=20, money=7)
# cappuccino = Coffee(water=200, milk=100, beans=12, money=6)

    def switcher(self, data=None):
        if self.state == "switch":
            print("What's your action? \n 1 - Buy, 2 - Fill, 3 - Take, 4 - Remaining, 5 - Exit")
            self.state = "action"
        elif self.state == "action":
            self.ask(data)


    def ask(self, user_action):
        if user_action in {"1", "buy"}:
            self.buy()
        elif user_action in {"2", "fill"}:
            self.fill()
        elif user_action in {"3", "take"}:
            self.take()
        elif user_action in {"4", "remaining"}:
            print(self)
            self.state = "switch"
            self.switcher()
        elif user_action in {"5", "exit"}:
            self.state = "exit"
            return
        # else:
        #    print("Write action (buy, fill, take, remaining, exit):")

# buy function offers 3 options: espresso, latte, cappuccino

    def buy(self):
        self.state = "switch"
        if self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
            self.switcher()
        drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:").strip()
        #  for each drink, test to ensure there are enough supplies.  If there are, subtract all and make the coffee.
        # else, report what is missing
        if drink == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
                return
            if self.beans < 16:
                print("Sorry, not enough beans!")
                return
            else:
                self.water -= 250
                self.beans -= 16
                self.disposable_cups -= 1
                self.money += 4
                print("I have enough resources, making you an espresso!")
                self.switcher()
        elif drink == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
                return
            if self.milk < 75:
                print("Sorry, not enough milk!")
                return
            if self.beans < 20:
                print("Sorry, not enough beans!")
                return
            else:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.disposable_cups -= 1
                self.money += 7
                print("I have enough resources, making you a latte!")
                self.switcher()
        elif drink == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
                return
            if self.milk < 100:
                print("Sorry, not enough milk!")
                return
            if self.beans < 12:
                print("Sorry, not enough beans!")
                return
            else:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.disposable_cups -= 1
                self.money += 6
                print("I have enough resources, making you a cappuccino!")
                self.switcher()
        else:
            self.switcher()

# fill method asks for quantities of water, milk, coffee beans, and disposable cups, then adds these to the balance

    def fill(self):
        self.state = "switch"
        fill_water = int(input("Write how many ml of water do you want to add:"))
        self.water += fill_water
        fill_milk = int(input("Write how many ml of milk do you want to add:"))
        self.milk += fill_milk
        fill_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        self.beans += fill_beans
        fill_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.disposable_cups += fill_disposable_cups
        self.switcher()

# take method reads money balance and removes it from machine

    def take(self):
        print("I gave you $", self.money)
        self.money = 0
        self.state = "switch"
        self.switcher()


machine = CoffeeMachine(
    water=100,
    milk=540,
    beans=120,
    disposable_cups=9,
    money=550,
    state="switch")

user_action = ""

while machine.state != "exit":
#while user_action != "exit"
    user_action = input().strip()
    machine.switcher(user_action)
