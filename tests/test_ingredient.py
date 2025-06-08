from praktikum.ingredient import Ingredient
from data import NameOfIngredients


class TestIngredient:

    def test_type_ingredient(self):

        type_ingredient = Ingredient(NameOfIngredients.INGREDIENT_ONE, NameOfIngredients.NAME_INGREDIENT_ONE, NameOfIngredients.PRICE_INGREDIENT_ONE)
        assert type_ingredient.type == NameOfIngredients.NAME_INGREDIENT_ONE

    def test_name_ingredient(self):

        name_ingredient = Ingredient(NameOfIngredients.INGREDIENT_ONE, NameOfIngredients.NAME_INGREDIENT_ONE, NameOfIngredients.PRICE_INGREDIENT_ONE)
        assert name_ingredient.name == NameOfIngredients.NAME_INGREDIENT_ONE

    def test_price_ingredient(self):

        price_ingredient = Ingredient(NameOfIngredients.INGREDIENT_ONE, NameOfIngredients.NAME_INGREDIENT_ONE, NameOfIngredients.PRICE_INGREDIENT_ONE)
        assert price_ingredient.price == NameOfIngredients.PRICE_INGREDIENT_ONE

    def test_get_price(self, burger_ingredient):
        price = burger_ingredient.get_price()
        assert price == NameOfIngredients.PRICE_INGREDIENT_ONE

    def test_get_price(self, burger_ingredient):
        assert burger_ingredient.get_price() == NameOfIngredients.PRICE_INGREDIENT_ONE

    def test_get_name(self, burger_ingredient):
        assert burger_ingredient.get_name() == NameOfIngredients.NAME_INGREDIENT_ONE

    def test_get_type(self, burger_ingredient):
        assert burger_ingredient.get_type() == NameOfIngredients.INGREDIENT_ONE
