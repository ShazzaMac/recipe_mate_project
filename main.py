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

calories, protein, carbs, fat = recipe_functions.calculateMacros(foods.rice, 200)#below unpacks the  returned values from a tuple into four separate variables. You can pass in any food so the function is reusable  and also adds an if/else condition 
if calories <= 500 and protein >= 30:
    print("Good high-protein option")
else:
    print("Does not meet requirements")
print("Calories:", calories)
print("Protein:", protein)
print("Carbs:", carbs)
print("Fat:", fat)


#if else statements to help track if a meal/recipe is within the users calorie allowance for the day 
serving = 0
if serving <= 0:
    print("serving size must be at least 1")
else:
    print("great, lets calculate with recipe mate!")

calories = 450
protein = 42
if calories <= 500 and protein >= 30:
    print("Within goal")
elif calories <= 700:
    print("Slightly above goal")
else :
    print("Well above goal")

calories = 550
protein = 35
if calories <= 600 and protein >= 30:
    print("High protein option")
elif calories <= 600 or protein >= 30:
    print("Meets one requirement")
else:
    print("Does not meet requirements")

    #if calories <= calorie_goal and protein >= protein_goal:  - save rthis for later 