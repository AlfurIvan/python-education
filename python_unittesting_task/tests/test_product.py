import pytest
from to_test import Product


@pytest.fixture()
def fix_product():
    fix_example = Product('something', 1000)
    return fix_example


def test_subtract_quantity(fix_product):
    fix_product.subtract_quantity()
    assert fix_product.quantity == 0


def test_add_quantity(fix_product):
    fix_product.add_quantity()
    assert fix_product.quantity == 2


@pytest.mark.parametrize("new_price",
                         [1337, 345, 632, 0, -3244])
def test_change_price(fix_product, new_price):
    fix_product.change_price(new_price)
    assert fix_product.price == new_price
