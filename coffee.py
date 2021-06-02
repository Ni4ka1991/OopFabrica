# coffee module

names = ("Espresso", "Cappuccino", "Robusta" )

class CoffeeMachine:
    def __init__( self, brand ):
        self.brand = brand
    
    def makeCoffee( self, name, ingredients ):
        return  _CoffeeDrink( name, ingredients )



class _CoffeeDrink:
    def __init__( self, name, ingredients ):
        self.name = name
        self.ingredients = ingredients

    def __str__( self ):
        return f"\nWe make you a coffee <{self.name}> with machine. Ingredients: {self.ingredients}.\n"

