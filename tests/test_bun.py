import pytest

from data import NameOfIngredients


class TestBuns:
    def test_get_buns_name(self, bun_r2_d3):
        assert bun_r2_d3.get_name() == NameOfIngredients.BUN_NAME

    def test_get_price(self, bun_r2_d3):
        assert bun_r2_d3.get_price() == NameOfIngredients.PRICE_BUN
        