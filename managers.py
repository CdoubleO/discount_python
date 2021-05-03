from typing import List
from .utils import ManagerKey, Nameable
from .product import Brand, Product
from .payment import Payment
from .discount import Discount

class PaymentManager(ManagerKey):
    def __init__(self):
        pass


class BrandManager(ManagerKey):
    def __init__(self):
        pass


class DiscountManager(ManagerKey):
    def __init__(self):
        pass


class ProductManager(ManagerKey):
    def __init__(self):
        pass

    def get_brand(self, brand: Brand) -> List[Product]:
        pass

    def get_tag(self, tag: str) -> List[Product]:
        pass


class Commerce(Nameable, ManagerKey):
    def __init__(self, name: str):
        pass

    def get_brand(self, brand) -> List[Product]:
        pass

    def get_tag(self, tag) -> List[Product]:
        pass


class MainManager():
    def __init__(self):
        pass

    def payments(self) -> PaymentManager:
        pass

    def discounts(self) -> DiscountManager:
        pass

    def brands(self) -> BrandManager:
        pass

    def products(self) -> ProductManager:
        pass

    def commerces(self) -> List[Commerce]:
        pass

    def add_payment(self, payment: Payment):
        pass

    def add_brand(self, brand: Brand):
        pass

    def add_product(self, product: Product):
        pass

    def add_commerce(self, commerce: Commerce):
        pass

    def add_discount(self, discount: Discount):
        pass
