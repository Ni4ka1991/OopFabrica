# coffee module

names = ("Espresso", "Cappuccino", "Robusta", "Latte", "Americano" )

class CoffeeMachine:
    def __init__( self, brand ):
        self.brand = brand
    
    def makeCoffee( self, name, ingredients ):
        if(names.count(name) != 0 ):
            return  _CoffeeDrink( name, ingredients )
        else:
            print(f"This machine can make only {name} types of Coffee." )
            input( "hit enter ... " )


class _CoffeeDrink:
    def __init__( self, name, ingredients ):
        self.name = name
        self.ingredients = ingredients

    def __str__( self ):
        return f"\nWe make you a coffee <{self.name}>. Ingredients: {self.ingredients}.\n"

