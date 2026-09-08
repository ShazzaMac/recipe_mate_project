#all app functions will be stored here 
import foods #imports the food.py file so it can be used by the printIngredientNames function 

def printIngredientNames(ingredients): #our parameter here is ingredients
        for ingredient in foods.ingredients:
            print("Ingredient:", ingredient["name"])