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

# a function that loops through all ingredients in a recipe and adds their values together using a for loop
#the function starts the 4 macros at 0 then as it loops through the ingredients it used calculateMacros() to accumulate the values together
def calculateRecipeMacros (ingredients):
      calories = 0 
      carbs = 0
      fat = 0
      protein = 0
      for ingredient in ingredients:
        calories_for_ingredient, protein_for_ingredient, carbs_for_ingredient, fat_for_ingredient = calculateMacros(ingredient, ingredient["quantity"])
        calories = calories + calories_for_ingredient
        protein = protein + protein_for_ingredient
        carbs = carbs + carbs_for_ingredient
        fat = fat + fat_for_ingredient
      return calories, protein, carbs, fat

def displayRecipe(recipe):
      return

def calculateProtein(protein_per_100g, grams):
         result = protein_per_100g * grams / 100
         return result   

#function to calculate the total protein of ingredients. ingredients is the parameter
def calculateTotalProtein(ingredient):
      total_protein = 0
      for ingredient in foods.ingredients:
            total_protein = total_protein + ingredient["protein"]
      return total_protein

#functions below are to help convert between metric and imperial measuremets. The first one is to convert ounces to grams --> this is currently limited to 6 options for the scope of the project but i could add more if i continue to build on the app at a later date
def ounces_to_grams(ounces):
     grams = ounces * 28.35
     return round(grams, 3) # returns the value as rounded to no more than 3 decimal places. This has been applied to all conversions for consistency.

def grams_to_ounces(grams):
     ounces = grams / 28.35
     return round(ounces, 3) 

def pounds_to_grams(pounds):
      grams = pounds * 453.592
      return round(grams, 3)

def cups_to_ml(cups):
      ml = cups * 236.588
      return round(ml,3)

def tablespoon_to_ml(tablespoon):
      ml = tablespoon * 14.787
      return round(ml,3)

def teaspoon_to_ml(teaspoon):
      ml = teaspoon * 4.929
      return round(ml,3)

#function uses the in operator to search - https://realpython.com/python-in-operator/ 
#https://www.codecademy.com/article/how-to-check-if-a-string-contains-a-substring-in-python
def searchRecipes(search_term):
    search_term = search_term.lower() #converts serach term to lower to help maximise the number of returned results 
    found = False
    for recipe_name in foods.featured_recipes:
        if search_term in recipe_name.lower(): #converts recipe name to lower
            print(recipe_name)
            found = True
    if found == False: #improves the user experience if no recipe matches are found by letting them know rather than returning straight to the menu 
        print("No recipes found containing that ingredient sorry!.")

searchRecipes("CHICKEN")