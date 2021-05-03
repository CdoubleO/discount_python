from typing import List
from .payment import Payment
from .product import Brand, Product, ProductInstance


class ShoppingBasketItem:
	def __init__(self, payment: Payment, product_instance: ProductInstance, count: int=1):
		pass

	def payment(self) -> Payment:
		pass

	def product_instance(self) -> ProductInstance:
		pass

	def count(self) -> int:
		pass

	def total(self) -> float:
		pass


class ShoppingBasket:
	def add_item(self, item: ShoppingBasketItem):
		pass

	def remove_item(self, item: ShoppingBasketItem):
		pass

	def items(self) -> List[ShoppingBasketItem]:
		return self._items

	def total(self) -> float:
		pass

	def total_discount(self) -> float:
		pass

	def net(self) -> float:
		pass

	def discounts(self) -> List['DiscountInstance']:
		return self._discounts

	def apply_discount(self, discount: 'Discount'):
		pass

	def has_discount_on_product(self, product: Product) -> bool:
		pass

	def has_discount_on_brand(self, brand: Brand) -> bool:
		pass
