#!/usr/bin/env python3

# MAIN MODULE
from os import system
from coffee import CoffeeDrink, CoffeeMachine

coffee_machine_1 = CoffeeMachine("Philips")
coffee_machine_2 = CoffeeMachine("Bosh")

coffee_1 = CoffeeMachine.makeCoffee( coffee_machine_1, "Cappuccino", ["water", "milk"] )
system( "clear" )
print(coffee_machine_1)
print(type(coffee_1))
print(coffee_1)
