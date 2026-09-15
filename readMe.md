# Recipe Mate

Welcome to **Recipe Mate**!

Recipe Mate is a Python-based recipe management application designed to help users manage recipes, serving sizes and nutritional information. The program can calculate calories and macronutrients, convert measurements from imperial to metric, and compare recipes against personal macro goals.

## Features

The user can:

1. **View recipes** – display the available recipes.
2. **Convert recipes** – convert supported imperial measurements into metric measurements.
3. **Change serving sizes** – scale a recipe to a different number of servings.
4. **Calculate macros** – calculate calories, protein, carbohydrates and fat for a recipe.
5. **Set macro goals** – enter personal calorie and macronutrient goals.
6. **Compare macros to goals** – check whether a recipe is within the user's chosen goals.
7. **Find recipes** – search the available recipes using a search term.
8. **Add recipes** – add a recipe name and serving size and save it to the recipe data file.
9. **Exit** – close the application.

## Project Structure

The project is divided into several Python files:

* `main.py` – contains the main menu and handles user input.
* `recipe.py` – contains the `Recipe` class, recipe methods and Recipe objects.
* `recipe_functions.py` – contains reusable functions for calculations, conversions, searching and CSV file handling.
* `foods.py` – contains ingredient and recipe data.
* `assessment_examples.py` – contains additional examples demonstrating Python concepts required by the course.
* `ingredients.csv` – stores ingredient nutritional information.
* `recipes.csv` – stores recipes added by the user.

## Data and Validation

RecipeMate uses CSV files to store data so that information can be loaded when the program starts. User input is validated using `try/except` blocks and conditional checks to prevent invalid values such as non-numeric or negative serving sizes.

The project also demonstrates Python programming concepts including functions, loops, conditionals, lists, dictionaries, tuples, sets, file handling, exception handling and object-oriented programming.

## Running the Program

Run the main program using:

python3 main.py

Follow the numbered menu options displayed in the terminal to use Recipe Mate.
