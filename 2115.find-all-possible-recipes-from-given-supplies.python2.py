# @leet start
from collections import deque


class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """

        # Track available ingredients and recipes
        available = set(supplies)

        # Queue to process recipe indices
        recipe_queue = deque(range(len(recipes)))
        created_recipes = []
        last_size = -1  # Tracks last known available count

        # Continue while we keep finding new recipes
        while len(available) > last_size:
            last_size = len(available)
            queue_size = len(recipe_queue)

            # Process all recipes in current queue
            while queue_size > 0:
                queue_size -= 1
                recipe_idx = recipe_queue.popleft()
                if all(
                    ingredient in available for ingredient in ingredients[recipe_idx]
                ):
                    # Recipe can be created - add to available items
                    available.add(recipes[recipe_idx])
                    created_recipes.append(recipes[recipe_idx])
                else:
                    recipe_queue.append(recipe_idx)

        return created_recipes


# @leet end

sol = Solution()
recipes = ["bread"]
ingredients = [["yeast", "flour"]]
supplies = ["yeast", "flour", "corn"]

recipes = ["bread", "sandwich"]
ingredients = [["yeast", "flour"], ["bread", "meat"]]
supplies = ["yeast", "flour", "meat"]

recipes = ["bread", "sandwich", "burger"]
ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
supplies = ["yeast", "flour", "meat"]

recipes = ["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"]
ingredients = [
    ["d"],
    ["hveml", "f", "cpivl"],
    ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
    ["cpivl", "hveml", "zpmcz", "ju", "h"],
    ["h", "fzjnm", "e", "q", "x"],
    ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"],
    ["f", "hveml", "cpivl"],
]
supplies = ["f", "hveml", "cpivl", "d"]
print(sol.findAllRecipes(recipes, ingredients, supplies))
