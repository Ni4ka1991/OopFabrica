#!/usr/bin/env python3

# MAIN MODULE
from os import system
from coffee import CoffeeMachine
from db import *
from coffee_house import *

brands = [ "Philips", "Bosch", "DeLonghi", "Saeco" ]
    
ingredients = []
replace_symb = ["[", "]", "'", " " ]



while True:
    option = printActionList( brands, "Coffee machine Brands:" )

    if( option == 1 ):
        print()

        opt = printActionList( list_maker( replace_symb, option - 1 ) , "Assortment of coffee:")
        
        if( opt > 0 and opt <= len(selectBrands_Coffee( option - 1 ))):
            quan = int(input( "How many cup of coffee do you whant? --> " ))
            print( f"You order {quan} cup of coffe {list_maker(replace_symb, option - 1)[opt - 1]}\n" )
            print( "List and quantity of ingredients:" )
            i = 0
            while i < len(kind_of_coffee[opt - 1]['Mocha']):
                print( f"{kind_of_coffee[opt - 1]['Mocha'][i]['name']} - {kind_of_coffee[opt - 1]['Mocha'][i]['quantity']}" )
                i += 1
            input("hit...")
        
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

