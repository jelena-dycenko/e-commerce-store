from typing import Dict
from product_basic_attributes import ProductBasicAttributes


class ShoppingCart:
    def __init__(self):
        self.__data: Dict[ProductBasicAttributes, int] = dict()

    def add(self, product, quantity):
        if product not in self.__data:
            self.__data[product] = 0
        if product.inventory == 0:
            print(f"{product.display_name} is out of stock")
        elif quantity > product.inventory:
            print(f"Inventory contains only {product.inventory}")
        else:
            product.reduce(quantity)
            self.__data[product] += quantity
            print(f'\nSuccessfully added {product.display_name} x{quantity}.')

    def show(self):
        if len(self.__data) == 0:
            print("Cart is empty")
        else:
            print(f"\nProduct\t\tPrice\tQuantity\tTotal")
            for key, value in self.__data.items():
                print(f"{key.display_name}\t\t${key.price} \t{value}\t\t\t${key.price * value}")
            print(f"----------------------------------------")
            print(f"Total amount:\t\t\t\t\t${self.amount}")

    @property
    def amount(self):
        ret = 0.0
        for key, value in self.__data.items():
            ret += key.price * value
        return int(ret)

    def empty(self):
        return len(self.__data) == 0

    def clear(self):
        return self.__data.clear()
