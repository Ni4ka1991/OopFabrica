#!/usr/bin/env python3

# MAIN MODULE
from os import system
from coffee import CoffeeMachine
from db import *
from coffee_house import *

brands = [ "Philips", "Bosch", "DeLonghi", "Saeco" ]# Philips -> Mocha (milk foam - 10 ml, stremed milk - 50 ml;, hot chocolate - 60 gr, espresso - 100 ml  -> )
    
ingredients = []
brands_


#philips ---> Mocha - 2 serving
#def coffeeBarista( ):
while True:
    option = printActionList( brands, "Coffee machine Brands:" )
    
    if( option == 1 ):
        loadInfo






































necessary_ingredients_index = [ 1, 2, 3, 4, 5 ]





















ingredients.append(createIngredientQuantity( 1, 2 ))
ingredients.append(createIngredientQuantity( 2, 20 ))
ingredients.append(createIngredientQuantity( 3, 22))
ingredients.append(createIngredientQuantity( 4, 25))
ingredients.append(createIngredientQuantity( 5, 18))



#    coffee_1 = CoffeeMachine.makeCoffee( CoffeeMachine(brands[brand_index]), coffee_type, coffee_ingredients )
#    print(coffee_1)

#system( "clear" )
#produceCoffee( 0, "Espresso" )
print( f"\
 {ingredients[0]['name']} - {ingredients[0]['quantity']} {ingredients[0]['unit']};\
 {ingredients[1]['name']} - {ingredients[1]['quantity']} {ingredients[1]['unit']};\
        ")
print()
print( kind_of_coffee )
