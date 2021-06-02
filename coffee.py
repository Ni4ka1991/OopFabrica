# coffee module

names = ("Espresso", "Cappuccino", "Robusta" )

class CoffeeMachine:
    def __init__( self, brand ):
        self.brand = brand
    
    def makeCoffee( self, name, ingredients ):
#        brand = self.brand
#        self.ingredients = ingredients
#        self.name = name
        _CoffeeDrink( name, ingredients )
#        return f"In coffee <{name}> used: {ingredients}."

#    def __str__( self ):
#        return f"\nWe make you a coffee <{self.name}> with machine < {self.brand} >. Ingredients: {self.ingredients}.\n"


class _CoffeeDrink:
    def __init__( self, name, ingredients ):
        self.name = name
        self.ingredients = ingredients

    def __str__( self ):
        return f"\nWe make you a coffee <{self.name}> with machine < {self.brand} >. Ingredients: {self.ingredients}.\n"

