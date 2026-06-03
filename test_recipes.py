import pytest
from recipes import Ingredient, Recipe

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