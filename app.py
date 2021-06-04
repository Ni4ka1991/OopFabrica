#!/usr/bin/env python3

# MAIN MODULE
from os import system
from coffee import CoffeeMachine
from db import *
from coffee_house import *

brands = [ "Philips", "Bosch", "DeLonghi", "Saeco" ]# Philips -> Mocha (milk foam, stremed milk, hot chocolate, espresso )
    
    
    if( brand_index == 0 ):
        necessary_ingredients_index = [ 0,  ]
    coffee_1 = CoffeeMachine.makeCoffee( CoffeeMachine(brands[brand_index]), coffee_type, coffee_ingredients )
    print(coffee_1)

system( "clear" )
#produceCoffee( 0, "Espresso" )
print( createIngredientQuantity( 0, 50 ))


