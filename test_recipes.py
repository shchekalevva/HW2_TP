import pytest
from recipes import Ingredient, Recipe, ShoppingList

def test_ingredient_init():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

    with pytest.raises(ValueError):
        Ingredient("Соль", -1.0, "г")
        
    with pytest.raises(ValueError):
        Ingredient("Сахар", 0.0, "г")

def test_ingredient_str():
    ing = Ingredient("Мука", 500.0, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_ingredient_eq():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 100.0, "г")
    ing3 = Ingredient("Крахмал", 500.0, "г")
    ing4 = Ingredient("Мука", 500.0, "кг")

    assert ing1 == ing2
    assert ing1 != ing3
    assert ing1 != ing4

def test_recipe_init():
    recipe = Recipe("Пицца")
    assert recipe.title == "Пицца"
    assert recipe.ingredients == []

def test_recipe_add_ingredient():
    recipe = Recipe("Пицца")
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Соль", 1.0, "г")
    ing3 = Ingredient("Мука", 200.0, "г")
    
    recipe.add_ingredient(ing1)
    recipe.add_ingredient(ing2)
    assert len(recipe.ingredients) == 2
    
    recipe.add_ingredient(ing3)
    assert len(recipe.ingredients) == 2
    assert recipe.ingredients[0].quantity == 700.0

def test_recipe_scale():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500.0, "г"))
    recipe1 = recipe.scale(1.5)
    
    assert recipe1 is not recipe
    assert recipe.ingredients[0].quantity == 500.0
    assert recipe1.ingredients[0].quantity == 750.0
    
    with pytest.raises(ValueError):
        recipe.scale(-67.0)
    with pytest.raises(ValueError):
        recipe.scale(0.0)

def test_recipe_len():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500.0, "г"))
    recipe.add_ingredient(Ingredient("Соль", 1.0, "г"))
    recipe.add_ingredient(Ingredient("Мука", 200.0, "г")) 
    
    assert len(recipe) == 2


    list_to_buy = ShoppingList()
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500.0, "г"))

    list_to_buy.add_recipe(recipe, 1.5)
    assert len(list_to_buy._items) == 1
    assert list_to_buy._items[0][1] == "Пицца"
    assert list_to_buy._items[0][0].quantity == 750.0

    with pytest.raises(ValueError):
        list_to_buy.add_recipe(recipe, -67.0)
    with pytest.raises(ValueError):
        list_to_buy.add_recipe(recipe, 0.0)

def test_shopping_list_remove_recipe():
    list_to_buy = ShoppingList()
    recipe1 = Recipe("Пицца")
    recipe1.add_ingredient(Ingredient("Мука", 500.0, "г"))
    
    recipe2 = Recipe("Пирог")
    recipe2.add_ingredient(Ingredient("Сахар", 100, "г"))

    list_to_buy.add_recipe(recipe1, 1.0)
    list_to_buy.add_recipe(recipe2, 1.0)

    list_to_buy.remove_recipe("Пицца")
    assert len(list_to_buy._items) == 1
    assert list_to_buy._items[0][1] == "Пирог"

    list_to_buy.remove_recipe("Запеканка")
    assert len(list_to_buy._items) == 1

def test_shopping_list_get_list():
    list_to_buy = ShoppingList()
    recipe1 = Recipe("Пицца")
    recipe1.add_ingredient(Ingredient("Мука", 500.0, "г"))
    recipe1.add_ingredient(Ingredient("Соль", 10.0, "г"))
    recipe2 = Recipe("Пирог")
    recipe2.add_ingredient(Ingredient("Мука", 300.0, "г"))
    recipe2.add_ingredient(Ingredient("Сахар", 100.0, "г"))

    list_to_buy.add_recipe(recipe1, 1.0)
    list_to_buy.add_recipe(recipe2, 1.5)

    final_list = list_to_buy.get_list()
    
    assert len(final_list) == 3
    assert final_list[0].name == "Мука"
    assert final_list[1].name == "Сахар"
    assert final_list[0].quantity == 950.0
    assert final_list[2].name == "Соль"

def test_shopping_list_add():
    list_to_buy1 = ShoppingList()
    recipe1 = Recipe("Пицца")
    recipe1.add_ingredient(Ingredient("Мука", 500.0, "г"))
    list_to_buy1.add_recipe(recipe1, 1.0)

    list_to_buy2 = ShoppingList()
    recipe2 = Recipe("Пирог")
    recipe2.add_ingredient(Ingredient("Сахар", 100.0, "г"))
    list_to_buy2.add_recipe(recipe2, 1.0)

    list_to_buy3 = list_to_buy1 + list_to_buy2
    assert len(list_to_buy1._items) == 1
    assert len(list_to_buy2._items) == 1
    assert len(list_to_buy3._items) == 2
