from typing import List, Tuple
from .utils import Nameable
from .product import Brand, Product, ProductInstance
from .shopping_basket import ShoppingBasket, ShoppingBasketItem


class DiscountInstance():
	def __init__(self, discount: 'Discount', product_instance: ProductInstance, amount: int, name: str=''):
		pass
	
	def name(self) -> str:
		pass

	def discount(self) -> 'Discount':
		pass

	def product_instance(self) -> ProductInstance:
		pass

	def amount(self) -> int:
		pass


class Discount(Nameable):
	def __init__(self, name: str, cummulative: bool,
				 condition: 'DiscountCondition'=None, effects: List['DiscountEffect']=[],
				 description: str=''):
		pass

	def cummulative(self) -> bool:
		pass

	def condition(self) -> 'DiscountCondition':
		pass
	
	def effects(self) -> List['DiscountEffect']:
		pass

	def description(self) -> str:
		pass

	def applicable(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> bool:
		pass

	def apply(self, shopping_basket: ShoppingBasket) -> List[DiscountInstance]:
		pass


class DiscountShoppingBasket(Discount):
	def __init__(self, name: str, cummulative: bool, condition: 'DiscountCondition', effects: List['DiscountEffect']):
		pass

	def applicable(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> bool:
		pass

	def apply(self, shopping_basket) -> List[DiscountInstance]:
		pass


class DiscountCondition():
	def __init__(self):
		pass

	def met(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> bool:
		raise NotImplementedError()


class DiscountEffect():
	def __init__(self):
		pass

	def apply(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> Tuple[float, str]:  # amount, name
		raise NotImplementedError()


class DiscountConditionMultiple(DiscountCondition):
	def add(self, condition: List[DiscountCondition]):
		pass


class DiscountConditionAnd(DiscountConditionMultiple):
	def met(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> bool:
		pass


class DiscountConditionOr(DiscountConditionMultiple):
	def met(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> bool:
		pass


class DiscountConditionProduct(DiscountCondition):
	def __init__(self, product: Product):
		pass

	def met(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> bool:
		pass


class DiscountConditionBrand(DiscountCondition):
	def __init__(self, brand: Brand):
		pass

	def met(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> bool:
		pass


class DiscountConditionTag(DiscountCondition):
	def __init__(self, tag: str):
		pass

	def met(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> bool:
		pass


class DiscountConditionPayment(DiscountCondition):
	def __init__(self, payment):
		DiscountCondition.__init__(self)
		self._payment = payment

	def met(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> bool:
		pass


class DiscountConditionMinimum(DiscountCondition):
	def __init__(self, minimum: int):
		pass

	def met(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> bool:
		pass


class DiscountEffectPercentage(DiscountEffect):
	def __init__(self, percentage: float, max_amount: int=-1):
		pass

	def percentage(self) -> float:
		pass

	def max_amount(self) -> int:
		pass

	def apply(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> Tuple[float, str]:
		pass


class DiscountEffectAmount(DiscountEffect):
	def __init__(self, amount: float, max_count: int=-1):
		pass

	def amount(self) -> float:
		pass

	def max_count(self) -> int:
		pass

	def apply(self, shopping_basket: ShoppingBasket, shopping_basket_item: ShoppingBasketItem) -> Tuple[float, str]:
		pass
