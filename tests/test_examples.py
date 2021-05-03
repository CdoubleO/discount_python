from .utils import TestData
from ..shopping_basket import ShoppingBasket, ShoppingBasketItem


def test_shopping_basket_example():
    test_data = TestData()

    data = test_data.manager('default')

    basket = ShoppingBasket()
    basket.add_item(ShoppingBasketItem(data.payments().get('Efectivo'),
                                       data.commerces().get('Coto').get('Melba'),
                                       3))
    basket.apply_discount(data.discounts().get('$5 en Melba'))

    assert basket.total() == 66.0
    assert basket.total_discount() == 15.0
    assert basket.net() == 51.0
