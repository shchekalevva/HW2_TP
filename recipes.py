class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name=name
        self.quantity=quantity 
        self.unit=unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        val=float(value)
        if val<=0:
            raise ValueError("Количество должно быть положительным")
        self._quantity=val

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, inother):
        if type(self)!=type(inother):
            return False
        return self.name==inother.name and self.unit==inother.unit
    
class Recipe:
    def __init__(self, title: str, ingredients=None):
        self.title = title
        if ingredients is not None:
            self.ingredients = ingredients
        else:
            self.ingredients = []

    def add_ingredient(self, ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                break
        else:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio) in (int, float):
            if ratio > 0:
                return True
        return False

    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
        ingredients1 = []
        for i in self.ingredients:
            scaled_quantity = i.quantity * ratio
            ingredient1 = Ingredient(i.name, scaled_quantity, i.unit)
            ingredients1.append(ingredient1)
        return Recipe(self.title, ingredients1)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        result = f"Рецепт блюда: {self.title}\nИнгредиенты:\n"
        for i in self.ingredients:
            result += f" - {i}\n"
        return result.strip()
    
class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        
        recipe1 = recipe.scale(portions)
        for ing in recipe1.ingredients:
            self._items.append((ing, recipe.title))

    def remove_recipe(self, title: str):
        items1 = [] 
        for item in self._items: 
            if item[1] != title: 
                items1.append(item)   
        self._items = items1

    def get_list(self):
        summary= {}
        for ing, _ in self._items:
            key = (ing.name, ing.unit)
            if key in summary:
                summary[key] += ing.quantity
            else:
                summary[key] = ing.quantity

        final = []
        for (name, unit), quantity in summary.items():
            final.append(Ingredient(name, quantity, unit))
            
        final.sort(key=lambda ing: ing.name)
        return final

    def __add__(self, other):
        result = ShoppingList()
        result._items.extend(self._items)
        result._items.extend(other._items)
        return result
    
class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        recipe2 = super().scale(ratio)
        return DietaryRecipe(recipe2.title, self.diet_type, recipe2.ingredients)

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"
    