#coffee_house module


from db import *
from os import system


ingredients    = loadInfo( "ingredients" )
kind_of_coffee = loadInfo( "kind_of_coffee" )

def createIngredientQuantity( ingredient_index, quantity ):    
    return {
            "name"     : ingredients[ingredient_index]['name'],
            "quantity" :  quantity,
            "unit"     : ingredients[ingredient_index]['unit']
            }

def printActionList( items, title = None ):
 
 system( "clear" )
 if( title != None ):
  print( "#" * 20 )
  print( title ) 
 print( "#" * 20 )
 for i in range( len( items ) ):
     print(
     f"{i + 1:2} {items[i]} "
  )
 print( "#" * 20 )
 
 option = int( input( " Select menu item >>> " ))
 return option
