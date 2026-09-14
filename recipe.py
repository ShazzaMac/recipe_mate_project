#this file contains the recipe class and its functions as well as any recipe objects like recipe1

# requires the following imports 
import foods
import recipe_functions

#initialises the class recipe and it's attributes
class Recipe:
    def __init__(self, name, ingredients, servings ):#initialising the object
        self.name = name
        self.ingredients = ingredients
        self.servings = servings

    def display(self):
        print("Recipe:", self.name)

#function to scale the recipe so that the amount of ingredients are enough for the number of servings required.
    def scale_recipe(self, new_serving):
        scaling_factor = new_serving / self.servings 
        for ingredient in self.ingredients:
            ingredient ["quantity"] = ingredient ["quantity"] * scaling_factor
        self.servings = new_serving

#function to display a list of the ingredients in the recipe
    def display_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient)

#function to convert any US measuremnets to UK measurements (or imperial to metric). They make use of the conversion functions inside the recipe_functions.py file
    def convert_measurements(self):
        for ingredient in self.ingredients:
            if ingredient ["unit"] == "ounces":
                grams = recipe_functions.ounces_to_grams(ingredient["quantity"])
                ingredient["quantity"] = grams
                ingredient["unit"] = "grams"
            elif ingredient["unit"] == "pounds":
                grams = recipe_functions.pounds_to_grams(ingredient["quantity"])
                ingredient["quantity"] = grams
                ingredient["unit"] = "grams"
            elif ingredient["unit"] == "cups":    
                ml = recipe_functions.cups_to_ml(ingredient["quantity"])
                ingredient["quantity"] = ml
                ingredient["unit"] = "ml"
            elif ingredient["unit"] == "tablespoon":
                ml = recipe_functions.tablespoon_to_ml(ingredient["quantity"])
                ingredient["quantity"] = ml
                ingredient["unit"] = "ml"  
            elif ingredient["unit"] == "teaspoons":   
                ml = recipe_functions.teaspoon_to_ml(ingredient["quantity"])
                ingredient["quantity"] = ml
                ingredient["unit"] = "ml"   


#below are the recipe objects
recipe1 = Recipe( "Mexican chicken + Rice", foods.ingredients, 4) #by importing foods i can import the ingedients without having to re-write them 

print(recipe1.name)
#can also be called as:
recipe1.display()
recipe1.convert_measurements()
recipe1.display_ingredients()

recipe1.scale_recipe(8)
print(recipe1.servings)


