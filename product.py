from typing import List
from .utils import Taggable, Nameable


class Brand(Nameable):
	pass


class Product(Taggable, Nameable):
    def __init__(self, brand: Brand, name: str, tags: List[str], description: str=''):
        pass

    def brand(self) -> Brand:
        pass

    def full_name(self) -> str:
        pass

    def description(self) -> str:
        pass


class ProductInstance():
	def __init__(self, product: Product, price: float):
		pass

	def price(self) -> float:
		pass

	def product(self) -> Product:
		pass
