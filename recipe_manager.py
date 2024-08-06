import json
from typing import Dict, List

# Define the recipe data structure
Recipe = Dict[str, List[str]]
Recipes = Dict[str, Recipe]

# Load recipes from file
def load_recipes() -> Recipes:
    try:
        with open("recipes.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save recipes to file
def save_recipes(recipes: Recipes) -> None:
    with open("recipes.json", "w") as file:
        json.dump(recipes, file)

# Add a new recipe
def add_recipe(recipes: Recipes) -> None:
    title = input("Enter recipe title: ")
    ingredients = get_list_from_input("Enter ingredients (leave blank to finish):")
    instructions = get_list_from_input("Enter instructions (leave blank to finish):")
    recipes[title] = {"ingredients": ingredients, "instructions": instructions}
    save_recipes(recipes)
    print(f"Recipe '{title}' added successfully!")

# Get a list of items from user input
def get_list_from_input(prompt: str) -> List[str]:
    print(prompt)
    items = []
    while True:
        item = input("> ")
        if not item:
            break
        items.append(item)
    return items

# View all recipes
def view_recipes(recipes: Recipes) -> None:
    if not recipes:
        print("No recipes found.")
        return
    print("Available recipes:")
    for title in recipes:
        print(f"- {title}")

# Search for recipes
def search_recipes(recipes: Recipes) -> None:
    query = input("Enter search query: ").lower()
    matches = [
        title for title, recipe in recipes.items()
        if query in title.lower() or any(query in ingredient.lower() for ingredient in recipe["ingredients"])
    ]
    if not matches:
        print(f"No recipes found for '{query}'.")
        return
    print(f"Recipes matching '{query}':")
    for title in matches:
        print(f"- {title}")

# Edit a recipe
def edit_recipe(recipes: Recipes) -> None:
    title = input("Enter recipe title: ")
    if title not in recipes:
        print(f"Recipe '{title}' not found.")
        return
    print(f"Editing recipe '{title}':")
    recipe = recipes[title]
    recipe["ingredients"] = get_list_from_input_list("Current ingredients:", recipe["ingredients"])
    recipe["instructions"] = get_list_from_input_list("Current instructions:", recipe["instructions"])
    save_recipes(recipes)
    print(f"Recipe '{title}' updated successfully!")

# Get a list of items from user input with current items displayed
def get_list_from_input_list(prompt: str, current_items: List[str]) -> List[str]:
    print(prompt)
    for i, item in enumerate(current_items, start=1):
        print(f"{i}. {item}")
    new_items = get_list_from_input("Enter new items (leave blank to keep current):")
    return new_items if new_items else current_items

# Delete a recipe
def delete_recipe(recipes: Recipes) -> None:
    title = input("Enter recipe title: ")
    if title not in recipes:
        print(f"Recipe '{title}' not found.")
        return
    del recipes[title]
    save_recipes(recipes)
    print(f"Recipe '{title}' deleted successfully!")

# Main program loop
def main() -> None:
    recipes = load_recipes()
    actions = {
        "1": add_recipe,
        "2": view_recipes,
        "3": search_recipes,
        "4": edit_recipe,
        "5": delete_recipe,
        "6": exit
    }
    while True:
        print("\nRecipe Manager")
        print("1. Add recipe")
        print("2. View recipes")
        print("3. Search recipes")
        print("4. Edit recipe")
        print("5. Delete recipe")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        action = actions.get(choice, None)
        if action:
            action(recipes)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
