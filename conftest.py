import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from data import NameOfIngredients


@pytest.fixture(scope='function')
def bun_r2_d3():
    name = NameOfIngredients.BUN_NAME
    price = NameOfIngredients.PRICE_BUN
    return Bun(name, price)


@pytest.fixture(scope='function')
def burger_ingredient():
    ingredient_type = NameOfIngredients.INGREDIENT_ONE
    ingredient_name = NameOfIngredients.NAME_INGREDIENT_ONE
    ingredient_price = NameOfIngredients.PRICE_INGREDIENT_ONE
    return Ingredient(ingredient_type, ingredient_name, ingredient_price)


@pytest.fixture(scope='function')
def data_base():
    return Database()
