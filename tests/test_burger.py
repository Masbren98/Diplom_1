from unittest.mock import Mock
from data import NameOfIngredients
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        first_bun = Mock()
        stellar_burger = Burger()
        stellar_burger.set_buns(first_bun)
        assert stellar_burger.bun == first_bun

    def test_add_ingredient(self):
        first_ingredient = Mock()
        second_ingredient = Mock()
        stellar_burger = Burger()
        stellar_burger.add_ingredient(first_ingredient)
        stellar_burger.add_ingredient(second_ingredient)
        assert stellar_burger.ingredients == [first_ingredient, second_ingredient]

    def test_remove_ingredient(self):
        first_ingredient = Mock()
        stellar_burger = Burger()
        first_ingredient.type = NameOfIngredients.INGREDIENT_ONE
        first_ingredient.name = NameOfIngredients.NAME_INGREDIENT_ONE
        first_ingredient.price = NameOfIngredients.PRICE_INGREDIENT_ONE
        stellar_burger.add_ingredient(first_ingredient)
        stellar_burger.remove_ingredient(0)
        assert len(stellar_burger.ingredients) == 0

    def test_move_ingredient(self):
        stellar_burger = Burger()
        first_ingredient = Mock()
        second_ingredient = Mock()
        stellar_burger.add_ingredient(first_ingredient)
        stellar_burger.add_ingredient(second_ingredient)
        stellar_burger.move_ingredient(0, 1)
        assert stellar_burger.ingredients == [second_ingredient, first_ingredient]

    def test_get_price(self):
        stellar_burger = Burger()
        first_bun = Mock()
        first_bun.get_price.return_value = 988
        first_ingredient = Mock()
        first_ingredient.get_price.return_value = 1337
        stellar_burger.bun = first_bun
        stellar_burger.ingredients = [first_ingredient]
        assert stellar_burger.get_price() == 988 * 2 + 1337

    def test_get_receipt(self):
        stellar_burger = Burger()
        first_bun = Mock()
        first_bun.get_name.return_value = NameOfIngredients.BUN_NAME
        first_ingredient = Mock()
        first_ingredient.get_type.return_value = NameOfIngredients.INGREDIENT_TWO
        first_ingredient.get_name.return_value = NameOfIngredients.NAME_INGREDIENT_TWO
        first_bun.get_price.return_value = 988
        first_ingredient.get_price.return_value = 1337
        stellar_burger.bun = first_bun
        stellar_burger.ingredients = [first_ingredient]
        expected_receipt = '(==== Флюоресцентная булка R2-D3 ====)\n= начинка Мясо бессмертных моллюсков Protostomia =\n(==== Флюоресцентная булка R2-D3 ====)\n\nPrice: 3313'
        assert stellar_burger.get_receipt() == expected_receipt
