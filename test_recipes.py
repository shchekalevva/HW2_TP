import pytest
from recipes import Ingredient

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