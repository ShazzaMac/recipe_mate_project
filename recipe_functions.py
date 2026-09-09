#all app functions will be stored here 
import foods #imports the food.py file so it can be used by the printIngredientNames function 

def printIngredientNames(ingredients): #our parameter here is ingredients
        for ingredient in foods.ingredients:
            print("Ingredient:", ingredient["name"])

def calculateCalories(calories_per_100g, grams): #function to calculate calories - calculated by the amount of calories whilst the grams is a percentage because all ingredients macros are based on 100g
    result = calories_per_100g * grams / 100
    return result            

def convertToMetric(amount, unit): #function to convert between metric and imperial units - requires amount and unit to perform calculation 
     result = amount/ unit
     return result            


def scaleRecipe(amount, servings):
      result = amount/ servings
      return result  

def calculateMacros(ingredient, grams): #here we are making use of dictionaries nside the function
      calories = ingredient["calories"] * grams / 100
      protein =  ingredient["protein"] * grams / 100
      carbs =  ingredient["carbs"] * grams / 100
      fat = ingredient["fat"] * grams / 100

      return calories, protein, carbs, fat

def displayRecipe(recipe):
      return

def calculateProtein(protein_per_100g, grams):
         result = protein_per_100g * grams / 100
         return result   