
#foods.py contains ingredients and ingredient dictionaries, featured recipes (one's i've already added to the program) and added recipes which will be added by the user
#uses dictionaries and lists. All values will be per 100g when being calculated for macros  - made up numbers to start with 
# ============================================================
# INGREDIENT DATA
# ============================================================

chicken = {
    "name" : "Chicken Breast",
    "calories" : 300,
    "protein" : 20,
    "carbs": 2,
    "fat" : 20,
    "quantity" : 200,
    "unit" : "grams"
}

pasta  = {
    "name" : "Pasta",
    "calories" : 340,
    "protein" : 5,
    "carbs": 22,
    "fat" : 10,
    "quantity" : 300,
    "unit" : "grams"
}

rice  = {
    "name" : "Rice",
    "calories" : 250,
    "protein" : 2,
    "carbs": 30,
    "fat" : 1,
    "quantity" : 4,
    "unit" : "ounces"
}


broccoli  = {
    "name" : "Broccoli",
    "calories" : 30,
    "protein" : 0,
    "carbs": 17,
    "fat" : 0.5,
   "quantity" : 200,
    "unit" : "grams"
}

pepper = {
    "name": "Pepper",
    "calories": 40,
    "protein": 0.2,
    "carbs": 6,
    "fat": 0,
    "quantity": 100,
    "unit": "grams"
}

cheese = {
    "name": "Cheese",
    "calories": 201,
    "protein": 16,
    "carbs": 12,
    "fat": 36,
    "quantity": 100,
    "unit": "grams"
}


sauce = {
    "name": "Sauce",
    "calories": 101,
    "protein": 6,
    "carbs": 32,
    "fat": 6,
    "quantity": 100,
    "unit": "grams"
}

#below i am creating a separate ingredient dictionary for the chicken item in chicken pasta so that if it's serving size gets updated it doesnt impact the chicken dictionary used by other recipe objects 
chicken_pasta_ingredient = {
    "name": "Chicken Breast",
    "calories": 300,
    "protein": 20,
    "carbs": 2,
    "fat": 20,
    "quantity": 200,
    "unit": "grams"
}

# ============================================================
# RECIPE INGREDIENT LISTS
# ============================================================

ingredients = [chicken, pasta, broccoli, rice]
#print(chicken, pasta, broccoli, rice)

mexican_chicken_rice = [
    chicken,
    rice,
    pepper,
]

chicken_pasta = [
    chicken_pasta_ingredient,
    pasta,
    cheese,
    sauce,
]

fish_tacos = [
   
]

# ============================================================
# RECIPE DATA
# ============================================================

# Pre-included recipe names displayed by the application.
featured_recipes = [
    "Mexican chicken + rice",
    "Air fried chicken + potatoes",
    "Biscoff and raspberry porridge",
    "Lentil and beef lasagne",
    "Lentil and beef bolognaise",
    "Boiled eggs, cottage cheese and toasted pitta",
    "Breakfast burrito - scrambled eggs, avocado, halloumi and cottage cheese",
    "Chicken and chickpea curry + rice",
    "Beef strip stirfry with bao buns and rice",
    "Chicken fajitas"
]

added_recipes = [] #this will be the collection of recipes added by the user 

# ============================================================
# ASSESSMENT DATA STRUCTURES
# ============================================================

#this will be a tuple because the measurements are fixed and this will stop a user from trying to change them
measurements = (
    "grams",
    "kilograms",
    "ounces",
    "pounds",
    "cups",
    "tablespoons",
    "teaspoons",
)

#example of a set - where every item is unique
ingredient_by_category = {"protein", "carbohydrate", "vegetable", "fruit", "dairy", "sugar"}