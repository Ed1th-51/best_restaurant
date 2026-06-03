from ingredient import Ingredient


class Recipe:
    def __init__(self, title, ingredients = None):
        self.title = title
        self.ingredients = ingredients if ingredients != None else []

    def add_ingredient(self, ingredient: Ingredient):
        for i in range(len(self.ingredients)):
            if  ingredient.__eq__(self.ingredients[i]):
                self.ingredients[i].quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return ratio.isdigit() and float(ratio) > 0
    
    def scale(self, ratio: float):
        scaled_recipe = Recipe(self.title)
        for i in range(len(self.ingredients)):
            scaled_recipe.add_ingredient(Ingredient(self.ingredients[i].name, self.ingredients[i].quantity*ratio, self.ingredients[i].unit))
        return scaled_recipe

    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        intermediate_stage = []
        for i in range(len(self.ingredients)):
            intermediate_stage.append(str(self.ingredients[i]))
        return f'{self.title}: {', '.join(intermediate_stage)}'
