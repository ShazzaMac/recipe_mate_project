#main file where everything will run 
import recipe_functions
import foods
import recipe

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

#print(foods.recipes [0:3])

#featured_recipes = foods.recipes[0:3]

#for recipe in featured_recipes:
  #  print(recipe)
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
"6. Compare macros to goals \n"
"7. Find recipes \n"
"8. Add recipes \n"
"9. Exit \n"
"====================")
    
    choice = input("Please enter a choice")
    if choice == "1":
        print("you have chosen to: View recipes")
        print("Available Recipes are :") 
        for recipe_name in foods.featured_recipes:
            print(recipe_name)

    elif choice == "2":
        print("you have chosen to: Convert recipes")
        recipe.recipe1.convert_measurements()
        recipe.recipe1.display_ingredients()

    elif choice == "3":
        print("you have chosen to: Change serving sizes")  
        try: #for this input i added a try/except to handle non-numerical input that cannot be converted to int
            new_serving = int(input("How many servings should the recipe cater for?"))# added int to make sure that any values are saved as an integer which is required for calculations
            if new_serving <= 0: #also catches any. negative values that the user may attempt to enter
                 print("Serving size must be greater than 0.")
            else:
                recipe.recipe1.scale_recipe(new_serving)
        except ValueError: # includes a message to help guide the user to type the correct input 
            print("Sorry, that isn't a valid choice. Please enter a whole number.")

    elif choice == "4":
        print("you have chosen to: Calculate macros")
        calories, protein, carbs, fat = recipe_functions.calculateRecipeMacros(recipe.recipe1.ingredients)
        print("Calories:", calories)
        print("Protein:", protein)
        print("Carbs:", carbs)
        print("Fat:", fat)

    elif choice == "5":
        print("you have chosen to: Set macro goals")
        calorie_goal = float(input("What is your daily calorie goal? "))
        protein_goal = float(input("What is your daily protein goal? "))
        carb_goal = float(input("What is your daily carbohydrate goal? "))
        fat_goal = float(input("What is your daily fat goal? "))
        if calorie_goal <=0 or protein_goal <=0 or carb_goal <=0 or fat_goal <=0:
           print("Sorry, that isn't a valid choice. Please enter a positive number.")
        else:
            print("your goals have been recorded as: ",calorie_goal, protein_goal, carb_goal, fat_goal )   

    elif choice == "6":
        print("you have chosen to: Compare recipe macros to goals")
        calories, protein, carbs, fat = recipe_functions.calculateRecipeMacros(recipe.recipe1.ingredients)
        if calories > calorie_goal:
            print("This recipe is not within your calorie goal.")
        else:
            print("This recipe is within your calorie goal -> great choice!")
        if fat > fat_goal:
            print("This recipe is not within your fat goal.")
        else:
            print("This recipe is within your fat goal -> great choice!")
        if carbs > carb_goal:
            print("This recipe is not within your carbs goal.")
        else:
            print("This recipe is within your carb goal -> great choice!")
        if protein > protein_goal:
            print("This recipe is not within your protein goal.")
        else:
            print("This recipe is within your protein goal -> great choice!")  

    elif choice == "7":
        print("you have chosen to: search recipes")
        search_term = input("What recipe would you like to search for? ")
        recipe_functions.searchRecipes(search_term)
        
    elif choice == "8":
        print("you have chosen to: Add recipes")
        recipe_name = input("What is the name of your recipe? ")

    elif choice == "9":
        print("you have chosen to: Exit")
        print("*-----------------*")
        print("Have a nice day! :)")
        print("*-----------------*")

    else:
        print("you have not chosen a valid option")


recipe_functions.ounces_to_grams(4)