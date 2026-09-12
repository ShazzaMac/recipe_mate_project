#this file contains the recipe class

class Recipe:
    def __init__(self, name, ingredients,method ):#initialising the object
        self.name = name,
        self.ingredients = ingredients,
        self.method = method,

#below are the recipe objects

recipe1 = Recipe( "Mexican chicken + Rice")
recipe2 = Recipe("Air fried chicken + potatoes")
recipe3 = Recipe("Chicken fajitas")

print(recipe1.name)