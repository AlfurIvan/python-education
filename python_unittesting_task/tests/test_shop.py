import pytest
from to_test import Shop, Product


@pytest.fixture()
def fix_shop():
    pr1 = Product('smth', 123, quantity=0)
    pr2 = Product('another_smth', 234, quantity=2)
    pr3 = Product('another_one', 345, quantity=2)
    pr4 = Product('another_one_two', 456, quantity=2)
    return Shop([pr1, pr2, pr3, pr4])


def test_add_product(fix_shop):
    new = Product('new', 98)
    fix_shop.add_product(new)
    assert new in fix_shop.products
    new_none = Product(None, None)
    fix_shop.add_product(new_none)
    assert new_none in fix_shop.products


@pytest.mark.parametrize("pr_title, i",
                         [('smth', 0),
                          ('another_smth', 1),
                          ('another_one', 2),
                          ('another_one_two', 3)])
def test__get_product_index(pr_title, i, fix_shop):
    s = fix_shop
    assert s._get_product_index(pr_title) == i


def test_sell_product(fix_shop):
    a = fix_shop
    try:
        a.sell_product('smth')
    except ValueError:
        assert True
    assert a.products[1].price == a.sell_product('another_smth')
    assert a.products[2].price * 2 == a.sell_product('another_one', qty_to_sell=2)
    assert a.products[2].price == a.sell_product('another_one_two')
    assert a.products[2].quantity == 1 and a.products[2].title == 'another_one_two'
