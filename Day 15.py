class Coffee_Machine:
    logo="""☕"""
    def __init__(self):
        self.resources={"Water": 300, "Milk":200, "Coffee": 100}
        self.money={"Penny":0.01, "Dime": 0.10, "Nickel":0.05, "Quarter":0.25}
        self.prices={"Espresso": 1.50, "Latte": 2.50, "Cappuccino":3.00}
    def choice(self):
        wish=input("What would you like? (espresso/latte/cappuccino.): ")
        if wish == "off":
            print("Turning off the machine. Goodbye!")
            exit()
        charge=input("Please insert coins. ")
        pennies=input("How many pennies? ")
        dimes=input("How many dimes? ")
        nickels=input("How many nickels? ")
        quarters=input("How many quarters? ")
        if wish == "report":
            return f"Water: {self.resources['Water']}ml\nMilk: {self.resources['Milk']}ml\nCoffee: {self.resources['Coffee']}g"  
        if wish == "espresso":
            if self.resources["Water"] <50:
                return "Sorry there is not enough water."
            elif self.resources["Coffee"] < 10:
                return "Sorry there is not enough coffee."
            else:
                overall_coins = (float(pennies) * self.money["Penny"] + 
                                float(dimes) * self.money["Dime"] + 
                                float(nickels) * self.money["Nickel"] + 
                                float(quarters) * self.money["Quarter"])
                if overall_coins >= self.prices["Espresso"]:
                    self.resources["Water"]-=50
                    self.resources["Coffee"]-=10
                    change=overall_coins-self.prices["Espresso"]
                    return f"Here, your espresso. Just enjoy drinking \nHere is ${change:.2f} in change"                
                else:
                    return "Sorry, that's not enough money. Money refunded."
        if wish == "latte":
            if self.resources["Water"] <200:
                return "Sorry there is not enough water."
            elif self.resources["Milk"] <150:
                return "Sorry there is not enough milk."
            elif self.resources["Coffee"] < 24:
                return "Sorry there is not enough coffee."
            else:
                overall_coins = (float(pennies) * self.money["Penny"] + 
                                float(dimes) * self.money["Dime"] + 
                                float(nickels) * self.money["Nickel"] + 
                                float(quarters) * self.money["Quarter"])
                if overall_coins >= self.prices["Latte"]:
                    self.resources["Water"]-=200
                    self.resources["Milk"]-=150
                    self.resources["Coffee"]-=24
                    change=overall_coins-self.prices["Latte"]
                    return f"Here, your Latte. Just enjoy drinking \nHere is ${change:.2f} in change"                
                else:
                    return "Sorry, that's not enough money. Money refunded."
        if wish == "cappuccino":
            if self.resources["Water"] <250:
                return "Sorry there is not enough water."
            elif self.resources["Milk"] <100:
                return "Sorry there is not enough milk."
            elif self.resources["Coffee"] < 24:
                return "Sorry there is not enough coffee." 
            else:
                overall_coins = (float(pennies) * self.money["Penny"] + 
                                float(dimes) * self.money["Dime"] + 
                                float(nickels) * self.money["Nickel"] + 
                                float(quarters) * self.money["Quarter"])
                if overall_coins >= self.prices["Cappuccino"]:
                    self.resources["Water"]-=250
                    self.resources["Milk"]-=100
                    self.resources["Coffee"]-=24
                    change=overall_coins-self.prices["Cappuccino"]
                    return f"Here, your cappuccino. Just enjoy drinking \nHere is ${change:.2f} in change"                
                else:
                    return "Sorry, that's not enough money. Money refunded."
my_machine=Coffee_Machine()
while True:
    result=my_machine.choice()
    if result:
        print(result)


