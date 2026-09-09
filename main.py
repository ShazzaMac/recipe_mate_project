#main file where everything will run 
import recipe_functions
import foods

recipe_functions.printIngredientNames(foods.ingredients) #prints the ingredients names

print(recipe_functions.calculateCalories(300, 150))    #relies on position of arguemnents

chicken_calories = recipe_functions.calculateCalories(300, 150)
print("chicken calories : " , chicken_calories)

chicken_protein = recipe_functions.calculateProtein(20, 150)
print("chicken protein : " , chicken_protein)

#update to above where we are now pulling the calories and protein value from the foods module 
chicken_calories = recipe_functions.calculateCalories( 
    foods.chicken["calories"], 150
)


chicken_protein = recipe_functions.calculateProtein(
    foods.chicken["protein"], 150
)

print("Chicken calories:", chicken_calories)
print("Chicken protein:", chicken_protein)

calories, protein = recipe_functions.calculateMacros(foods.chicken, 150)#below unpacks the two returned values
print("Calories:", calories)
print("Protein:", protein)