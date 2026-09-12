#uses dictionaries and lists. All values will be per 100g - made up numbers to start with 

chicken = {
    "name" : "Chicken Breast",
    "calories" : 300,
    "protein" : 20,
    "carbs": 2,
    "fat" : 20
}

pasta  = {
    "name" : "Pasta",
    "calories" : 340,
    "protein" : 5,
    "carbs": 22,
    "fat" : 10
}

rice  = {
    "name" : "Rice",
    "calories" : 250,
    "protein" : 2,
    "carbs": 30,
    "fat" : 1
}


broccoli  = {
    "name" : "Broccoli",
    "calories" : 30,
    "protein" : 0,
    "carbs": 17,
    "fat" : 0.5
}

ingredients = [chicken, pasta, broccoli, rice]
#print(chicken, pasta, broccoli, rice)

recipes = [
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