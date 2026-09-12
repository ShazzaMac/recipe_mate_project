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
calorie_goal = 400
protein_goal = 30
high_calorie_limit = 700
if calories <= calorie_goal and protein >= protein_goal:
    print("Within goal")
elif calories <= high_calorie_limit:
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
servings = 2
if servings == 4:
    print("This recipe serves four")
else:
    print("This recipe does not serve four")

servings = 0
if not servings:
    print("No servings entered")

recipe_found = False
if not recipe_found:
    print("No recipe found")
else:
    print("Recipe found")    

calorie_goal = 600
protein_goal = 3
calories, protein, carbs, fat = recipe_functions.calculateMacros(foods.rice, 200)#below unpacks the  returned values from a tuple into four separate variables. You can pass in any food so the function is reusable  and also adds an if/else condition 
if calories <= calorie_goal and protein_goal >= protein_goal:
    print("Recipe meets your goals")
else:
    print("Recipe does not meet your goals")    


#working on for loops 
for ingredient in foods.ingredients:
    print(ingredient["name"])

#for loop to add calories for ingredients 
total_calories = 0
for ingredient in foods.ingredients:
    total_calories = total_calories + ingredient ["calories"]
print("Total calories:", total_calories)

#for loop to add protein for ingredients 
total_protein = 0
for ingredient in foods.ingredients:
    total_protein = total_protein + ingredient ["protein"]
print("Total protein:", total_protein)

#using it is a function 
total_protein = recipe_functions.calculateTotalProtein(foods.ingredients)
print("Total protein:", total_protein)

print(foods.recipes [0:3])

featured_recipes = foods.recipes[0:3]

for recipe in featured_recipes:
    print(recipe)
#building the menu with a while loop and if/else statements
# --------------------------------------------------------
choice = ""
while choice != "8":
    print( "==================== \n" 
     "RecipeMate \n" 
"==================== \n"
"1. View recipes \n"
"2. Convert recipes \n"
"3. Change serving sizes \n"
"4. Calculate macros \n"
"5. Set macro goals \n"
"6. Find recipes \n"
"7. Add recipes \n"
"8. Exit \n"
"====================")
    
    choice = input("Please enter a choice")
    if choice == "1":
        print("you have chosen to: View recipes")
        print("Available Recipes are :") 
        for recipe in foods.recipes:
            print(recipe)
    elif choice == "2":
        print("you have chosen to: Convert recipes")
    elif choice == "3":
        print("you have chosen to: Change serving sizes")   
    elif choice == "4":
        print("you have chosen to: Calculate macros")
    elif choice == "5":
        print("you have chosen to: Set macro goals")
    elif choice == "6":
        print("you have chosen to: Find recipes")
    elif choice == "7":
        print("you have chosen to: Add recipes")
    elif choice == "8":
        print("you have chosen to: Exit")
    else:
        print("you have not chosen a valid option")
