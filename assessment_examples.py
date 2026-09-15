
import foods
import recipe_functions

# ============================================================
# FUNCTION AND ARGUMENT EXAMPLES
# ============================================================

recipe_functions.printIngredientNames(foods.ingredients)

# Demonstrates positional arguments.
print(recipe_functions.calculateCalories(300, 150))

chicken_calories = recipe_functions.calculateCalories(300, 150)
print("Chicken calories:", chicken_calories)

chicken_protein = recipe_functions.calculateProtein(20, 150)
print("Chicken protein:", chicken_protein)

# Pull the protein value from the foods module.
chicken_protein = recipe_functions.calculateProtein(foods.chicken["protein"], 150)

# Pull the calorie value from the foods module.
chicken_calories = recipe_functions.calculateCalories(foods.chicken["calories"], 150)

print("Chicken calories:", chicken_calories)
print("Chicken protein:", chicken_protein)

# ============================================================
# TUPLE UNPACKING AND CONDITIONAL EXAMPLE
# ============================================================

# calculateMacros returns four values in a tuple.
# These values are unpacked into four separate variables.
calories, protein, carbs, fat = recipe_functions.calculateMacros(foods.rice, 200)

if calories <= 500 and protein >= 30:
    print("Good high-protein option")
else:
    print("Does not meet requirements")

print("Calories:", calories)
print("Protein:", protein)
print("Carbs:", carbs)
print("Fat:", fat)

# ============================================================
# LOOP AND DATA STRUCTURE EXAMPLES
# ============================================================

# Demonstrates a for loop through a list of recipe names.
for recipe_name in foods.featured_recipes:
    print(recipe_name)

# Demonstrates a default parameter.
print(recipe_functions.calculateCalories(300, 200))
print(recipe_functions.calculateCalories(300))

# Demonstrates a set.
print(foods.ingredient_by_category)

# Demonstrates list slicing.
print(foods.featured_recipes[0:3])

# Demonstrates exponentiation.
print(2**3)

# Demonstrates floor division.
print(17 // 5)

# ============================================================
# IF / ELIF / ELSE AND BOOLEAN LOGIC EXAMPLES
# ============================================================

serving = 0
if serving <= 0:
    print("Serving size must be at least 1")
else:
    print("Great, let's calculate with RecipeMate!")


calories = 450
protein = 42
calorie_goal = 400
protein_goal = 30
high_calorie_limit = 700

if calories <= calorie_goal and protein >= protein_goal:
    print("Within goal")
elif calories <= high_calorie_limit:
    print("Slightly above goal")
else:
    print("Well above goal")


calories = 550
protein = 35
if calories <= 600 and protein >= 30:
    print("High protein option")
elif calories <= 600 or protein >= 30:
    print("Meets one requirement")
else:
    print("Does not meet requirements")


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

# ============================================================
# MACRO AND FOR LOOP EXAMPLES
# ============================================================

calorie_goal = 600
protein_goal = 30
calories, protein, carbs, fat = recipe_functions.calculateMacros(foods.rice, 200)
if calories <= calorie_goal and protein >= protein_goal:
    print("Recipe meets your goals")
else:
    print("Recipe does not meet your goals")


# Demonstrates a for loop through ingredient dictionaries.
for ingredient in foods.ingredients:
    print(ingredient["name"])


# Demonstrates a for loop used to calculate a total.
total_calories = 0

for ingredient in foods.ingredients:
    total_calories = total_calories + ingredient["calories"]

print("Total calories:", total_calories)


# Demonstrates another for loop used to calculate a total.
total_protein = 0

for ingredient in foods.ingredients:
    total_protein = total_protein + ingredient["protein"]

print("Total protein:", total_protein)


# Demonstrates using a reusable function instead of calculating
# the total directly in the main program.
total_protein = recipe_functions.calculateTotalProtein(foods.ingredients)

print("Total protein:", total_protein)
