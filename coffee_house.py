#coffee_house module


from db import *

ingredients    = loadInfo( "ingredients" )
kind_of_coffee = loadInfo( "kind_of_coffee" )

def createIngredientQuantity( ingredient_index, quantity ):    
    return {
            "name"     : ingredients[ingredient_index]['name'],
            "quantity" :  quantity,
            "unit"     : ingredients[ingredient_index]['unit']
            }
