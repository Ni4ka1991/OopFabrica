#!/usr/bin/env python3

# MAIN MODULE
from os import system
from coffee import CoffeeMachine
from db import *

ingredients = loadInfo("ingredients")

ingredients_as_list = dataConversion(ingredients)

brands = [ "Philips", "Bosch", "DeLonghi", "Saeco" ]


coffee_machine_1 = CoffeeMachine(brands[0])
coffee_machine_2 = CoffeeMachine(brands[1])

coffee_1 = CoffeeMachine.makeCoffee( coffee_machine_1, "Espresso", ingredients_as_list[0] )

system( "clear" )
print(coffee_1)

