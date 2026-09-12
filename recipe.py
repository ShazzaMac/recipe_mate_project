#this file contains the recipe class
import foods

class Recipe:
    def __init__(self, name, ingredients, servings ):#initialising the object
        self.name = name
        self.ingredients = ingredients
        self.servings = servings

    def display(self):
        print("Recipe:", self.name)

    def scale_recipe(self, new_serving):
        self.servings = new_serving

    def display_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient)


#below are the recipe objects
recipe1 = Recipe( "Mexican chicken + Rice", foods.ingredients, 4) #by importing foods i can import the ingedients without having to re-write them 
#recipe2 = Recipe("Air fried chicken + potatoes", foods.ingredients)
#recipe3 = Recipe("Chicken fajitas", foods.ingredients)

print(recipe1.name)
#print(recipe2.name)
#print(recipe3.name)

recipe1.display()
#recipe2.display()
#recipe3.display()

recipe1.scale_recipe(8)
print(recipe1.servings)

recipe1.display_ingredients()