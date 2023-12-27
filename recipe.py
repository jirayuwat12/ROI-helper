import json
import os

def get_recipe(version = "2130"):
    FOLDER_PATH = os.path.join(os.getcwd(), "recipe", version)

    recipe = {}
    for file in os.listdir(FOLDER_PATH):
        if file.endswith(".json"):
            with open(os.path.join(FOLDER_PATH, file), "r") as f:
                recipe.update(json.load(f))
    return recipe

if __name__ == "__main__":
    recipe = get_recipe()
    print(recipe)