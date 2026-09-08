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
print(chicken["fat"])
print(ingredients[1]["name"])

#practising for loop

for ingredient in ingredients:
    print("Ingredient:", ingredient["name"])