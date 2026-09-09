#main file where everything will run 
import recipe_functions
import foods

recipe_functions.printIngredientNames(foods.ingredients) #prints the ingredients names

print(recipe_functions.calculateCalories(300, 150))    