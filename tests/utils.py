from ..managers import MainManager, Commerce
from ..product import Brand, Product, ProductInstance
from ..payment import Payment
from ..discount import Discount, DiscountConditionBrand, DiscountConditionProduct, DiscountEffectPercentage, DiscountEffectAmount


class TestData():
    def __init__(self):
        self._data = {}

        data = MainManager()

        data.add_brand(Brand('Bagley'))
        data.add_brand(Brand('Terrabussi'))

        data.add_product(Product(data.brands().get('Bagley'), 'Sonrisas', ['alimento', 'galletitas', 'chatarra'], 'Caritas rellenas de frambuesa'))
        data.add_product(Product(data.brands().get('Bagley'), 'Panchitas', ['alimento', 'galletitas', 'chatarra'], 'Caritas de chocolate rellenas de crema'))
        data.add_product(Product(data.brands().get('Terrabussi'), 'Melba', ['alimento', 'galletitas', 'chatarra'], 'Galletitas de chocolate rellenas de crema'))
        data.add_product(Product(data.brands().get('Duquesa'), 'Melba', ['alimento', 'galletitas', 'chatarra'], 'Galletitas de vainilla rellenas de crema'))

        data.add_payment(Payment('Efectivo'))
        data.add_payment(Payment('Visa'))
        data.add_payment(Payment('Mastercard'))

        coto = Commerce('Coto')
        coto.add(ProductInstance(data.products().get('Sonrisas'), 20.0))
        coto.add(ProductInstance(data.products().get('Melba'), 22.0))

        carrefour = Commerce('Carrefour')
        carrefour.add(ProductInstance(data.products().get('Duquesa')), 18.0)
        carrefour.add(ProductInstance(data.products().get('Melba')), 23.0)

        dia = Commerce('Dia')
        dia.add(ProductInstance(data.products().get('Panchitas'), 16.0))
        dia.add(ProductInstance(data.products().get('Duquesa'), 20.0))

        data.add_commerce(coto)
        data.add_commerce(carrefour)
        data.add_commerce(dia)

        bagley_discount = Discount('20% Bagley',
                                    True,
                                    DiscountConditionBrand(data.brands().get('Bagley')),
                                    [DiscountEffectPercentage(20.0)],
                                    R'20% de descuento en productos Bagley')

        melba_discount = Discount('$5 en Melba',
                                    True,
                                    DiscountConditionProduct(data.products().get('Melba')),
                                    [DiscountEffectAmount(5.0, 5)],
                                    R'$5 en Melba (maximo 5 unidades)')

        data.add_discount(bagley_discount)
        data.add_discount(melba_discount)

        self.add_data_manager('default', data)

    def add_data_manager(self, name: str, data_set: MainManager):
        self._data[name] = data_set

    def manager(self, with_name: str) -> MainManager:
        return self._data.get(with_name)
