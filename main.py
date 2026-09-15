# Main program file. Runs the menu and handles user input.
import recipe_functions
import foods
import recipe

# Loads saved recipe and ingredient data when the program starts.
csv_recipes = recipe_functions.loadRecipes()

# --------------------------------------------------------
# Main menu loop. The program continues until the user chooses Exit
# Makes use of a while loop and if/else statements and
# Keeps the menu running until the user chooses Exit.
# --------------------------------------------------------
calorie_goal = None
protein_goal = None
carb_goal = None
fat_goal = None

choice = ""
while choice != "9":
    print( "==================== \n" 
     "Recipe Mate \n" 
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
"==================== \n"
"==================")
    
    choice = input("Please enter a choice... ")
    if choice == "1":
        print("you have chosen to: View recipes")
        print("Available Recipes are: ") 
        for recipe_name in foods.featured_recipes:#shows the featured recipes
            print(recipe_name)
        for added_recipe in foods.added_recipes: #allows the user to see their added recipe in the list when option 1 is selected after option 8
            print(added_recipe)
        for saved_recipe in csv_recipes:#shows the recipes from the recipes csv file 
            print(saved_recipe["name"]) 

    elif choice == "2":
        print("you have chosen to: Convert recipes ")
        recipe.recipe1.convert_measurements()
        recipe.recipe1.display_ingredients()

    elif choice == "3":
        print("you have chosen to: Change serving sizes ")  
        try: #for this input i added a try/except to handle non-numerical input that cannot be converted to int
            new_serving = int(input("How many servings should the recipe cater for? "))# added int to make sure that any values are saved as an integer which is required for calculations
            if new_serving <= 0: #also catches any. negative values that the user may attempt to enter
                 print("Serving size must be greater than 0.")
            else:
                recipe.recipe1.scale_recipe(new_serving)
        except ValueError: # includes a message to help guide the user to type the correct input 
            print("Sorry, that isn't a valid choice. Please enter a whole number.")

    elif choice == "4":
        print("you have chosen to: Calculate macros ")
        calories, protein, carbs, fat = recipe_functions.calculateRecipeMacros(recipe.recipe1.ingredients)
        print("Calories:", calories)
        print("Protein:", protein)
        print("Carbs:", carbs)
        print("Fat:", fat)

    elif choice == "5":
        print("you have chosen to: Set macro goals ")
        try:#a try/except block to prevent the user from trying to use non-numerical values 
         calorie_goal = float(input("What is your daily calorie goal? "))
         protein_goal = float(input("What is your daily protein goal? "))
         carb_goal = float(input("What is your daily carbohydrate goal? "))
         fat_goal = float(input("What is your daily fat goal? "))
         if calorie_goal <=0 or protein_goal <=0 or carb_goal <=0 or fat_goal <=0:
           print("Sorry, that isn't a valid choice. Please enter a positive number.")
         else:
           print("your goals have been recorded as: ",calorie_goal, protein_goal, carb_goal, fat_goal )   
        except ValueError:
          print("Sorry, please enter numbers only.")
      

    elif choice == "6":
        print("you have chosen to: Compare recipe macros to goals")

        if calorie_goal is None: #had to put this in to prevent users from trying to compare goals before setting them 
            print("Please set your macro goals first using option 5.")
        else:
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

    #uses the search recipe function to find a substring in a string
    elif choice == "7":
        print("you have chosen to: search recipes ")
        search_term = input("What recipe would you like to search for? ")
        recipe_functions.searchRecipes(search_term)
        
    elif choice == "8":
        print("you have chosen to: Add recipes ")
        recipe_name = input("What is the name of your recipe? ")
        #another try/except added to prevent invalid input
        try:
            servings = int(input("How many servings does the recipe make? "))
            if servings <= 0:
             print("Serving size must be greater than 0.")
            else:
             recipe_functions.saveRecipe(recipe_name, servings)
             foods.added_recipes.append(recipe_name)
            # By using an f-string, the program displays the name of the recipe in the confirmation message.
             print(f"{recipe_name} has been added successfully to Recipe Mate!")
        except ValueError:
            print("Sorry, that isn't a valid number. Please enter a whole number instead.")

    elif choice == "9":
        print("you have chosen to: Exit ")
        print("*-----------------*")
        print("Have a nice day! :)")
        print("*-----------------*")

    else:
        print("you have not chosen a valid option")


