
#foods.py contains ingredients and ingredient dictionaries, featured recipes (one's i've already added to the program) and added recipes which will be added by the user
#uses dictionaries and lists. All values will be per 200g - made up numbers to start with 

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
    "quantity" : 200,
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

ingredients = [chicken, pasta, broccoli, rice]
#print(chicken, pasta, broccoli, rice)
# a list of pre - included recipes --> note to self changed the name from recipes to featured_recipes to prevent confusion with recipe class and objects
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