#all app functions will be stored here including calculations and conversions 
import foods #imports the food.py file so it can be used by the printIngredientNames function 
import csv # built -in python module so we can use csv data 

# ============================================================
# CSV DATA FUNCTIONS
# ============================================================

def loadIngredients():
     with open("ingredients.csv", "r") as file: #opens the csv for reading and 'with' makes sure the file is closed after using
          reader = csv.DictReader(file) #this line reads each row and uses the column headings as dictionary keys
          ingredients = []#puts each read row into a list
          for row in reader:
               row["calories"] = float(row["calories"])#these next 4 lines convert the four nutritional values from strings to floats so they can be correctly used in calculations. If left as strings they would cause errors 
               row["protein"] = float(row["protein"])
               row["carbs"] = float(row["carbs"])
               row["fat"] = float(row["fat"])
               ingredients.append(row)
     return ingredients# returns the list so it can be used by the program 

#This function saves a users recipe to teh recipe csv file - it requires the user to provide a recipe name and serving size
def saveRecipe(recipe_name, servings):
     with open("recipes.csv", "a", newline="") as file: #a is used to append recipes to teh list and newline is to prevent blank lines from appearing within the csv records. 
          writer = csv.writer(file)
          writer.writerow([recipe_name, servings])
          

#This function loads saved recipes so they dont disappear after the program is closed.
def loadRecipes():
      with open("recipes.csv", "r") as file: #r signifies that the file will be read 
           reader = csv.DictReader(file)
           recipes = [] # stores the recipes 
           for row in reader:# loops through the rows of recipes 
             row["servings"] = int(row["servings"])#converts the servings from strings to integers to allow for calculations later 
             recipes.append(row)
      return recipes

# ============================================================
# RECIPE AND MACRO FUNCTIONS
# ============================================================

def printIngredientNames(ingredients): #our parameter here is ingredients
        for ingredient in ingredients:
            print("Ingredient:", ingredient["name"])

def calculateCalories(calories_per_100g, grams = 100):
     #function to calculate calories - calculated by the amount of calories whilst the grams is a percentage because all ingredients macros are based on 100g. The default parameter for grams is also 100
    """Calculate calories based on calories per 100g and the amount in grams."""
    result = calories_per_100g * grams / 100
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
      """Calculate the total calories, protein, carbs and fat for a recipe.""" 
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

# ============================================================
# MEASUREMENT CONVERSION FUNCTIONS
# ============================================================

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

def convertToMetric(amount, unit): #function to convert between metric and imperial units - requires amount and unit to perform calculation 
     result = amount/ unit
     return result 

# ============================================================
# SEARCH AND COMPARISON FUNCTIONS
# ============================================================

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

#searchRecipes("CHICKEN")

def compareRecipes(recipe_a, recipe_b):
    """Compare the calorie totals of two recipes. Creates tuples"""
    recipe_a_macros =calculateRecipeMacros(recipe_a.ingredients)
    recipe_b_macros = calculateRecipeMacros(recipe_b.ingredients)
    recipe_a_calories = recipe_a_macros[0]
    recipe_b_calories = recipe_b_macros[0]
    """Returns the string responses rather than printing them """
    if recipe_a_calories < recipe_b_calories:
        return f"{recipe_a.name} has fewer calories than {recipe_b.name}."
    elif recipe_b_calories < recipe_a_calories:
        return f"{recipe_b.name} has fewer calories than {recipe_a.name}."
    else:
        return "Both recipes have the same number of calories."
    
# ============================================================
# PRACTICE /  ADDITIONAL ASSESSMENT FUNCTIONS
## These functions demonstrate additional Python techniques
# that could be integrated into future versions of RecipeMate.
# They are retained as evidence of additional assessment requirements.
# ============================================================
def displayRecipe(recipe):
      return           

def scaleRecipe(amount, servings):
      result = amount/ servings
      return result  

def calculateProtein(protein_per_100g, grams):
         result = protein_per_100g * grams / 100
         return result   

#function to calculate the total protein of ingredients. ingredients is the parameter
def calculateTotalProtein(ingredients):
      total_protein = 0
      for ingredient in ingredients:
            total_protein = total_protein + ingredient["protein"]
      return total_protein
