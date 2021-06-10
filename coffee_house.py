#coffee_house module


from db import *
from os import system


ingredients    = loadInfo( "ingredients" )
kind_of_coffee = loadInfo( "kind_of_coffee" )
brands_assortment_coffee = loadInfo( "brands_assortment_coffee" )

def createIngredientQuantity( ingredient_index, quantity ):    
    return {
            "name"     : ingredients[ingredient_index]['name'],
            "quantity" :  quantity,
            "unit"     : ingredients[ingredient_index]['unit']
            }


def selectBrands_Coffee( index ):
    return f"{brands_assortment_coffee[ index ]['assortment']}"


def list_maker( replace_symb, key ):
        return replaceSymbols( replace_symb, selectBrands_Coffee( key ))


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
 print( f" For exit enter {len(items) + 1}" )
 print( "#" * 20 )
 
 option = int( input( " Select menu item >>> " ))
 return option


def replaceSymbols( symb_list, string ):
    i = 0
    while i < len(symb_list):
        string = string.replace( symb_list[i], "" )
        i += 1
    
    split_string = string.split(",")

    return split_string






























