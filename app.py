#!/usr/bin/env python3

# MAIN MODULE
from os import system
from coffee import CoffeeMachine
from db import *
from coffee_house import *

brands = [ "Philips", "Bosch", "DeLonghi", "Saeco" ]
    
ingredients = []
replace_symb = ["[", "]", "'", " " ]


#def coffeeBarista( ):
while True:
    option = printActionList( brands, "Coffee machine Brands:" )

    if( option == 1 ):
        print()

        opt = printActionList( list_maker( replace_symb, option - 1 ) , "Assortment of coffee:")
        
        if( opt > 0 and opt <= len(selectBrands_Coffee( option - 1 ))):
            quan = int(input( "How many cup of coffee do you whant? --> " ))
            print( f"You order {quan} cup of coffe {list_maker(replace_symb, option - 1)[opt - 1]}" )

        
        else:
            print("Enter correct value")
    
    elif( option == 2 ):
        print()
        printActionList( replaceSymbols( replace_symb, selectBrands_Coffee( option - 1 )), "Assortment of coffee:")
    
    elif( option == 3 ):
        print()
        printActionList( replaceSymbols( replace_symb, selectBrands_Coffee( option - 1 )), "Assortment of coffee:")
        
    elif( option == 4 ):
        print()
        printActionList( replaceSymbols( replace_symb, selectBrands_Coffee( option - 1 )), "Assortment of coffee:")

    elif( option == 5 ):
        break
#        print("bla - bla - bla")
#        input( "hit ..." )
    
    else:
        raise ValueError
        print( "Enter one of menu item..." )


print( f"\
 {ingredients[0]['name']} - {ingredients[0]['quantity']} {ingredients[0]['unit']};\
 {ingredients[1]['name']} - {ingredients[1]['quantity']} {ingredients[1]['unit']};\
        ")
print()
#print( kind_of_coffee )
