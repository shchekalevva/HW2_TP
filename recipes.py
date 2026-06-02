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