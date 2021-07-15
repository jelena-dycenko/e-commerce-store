from product_basic_attributes import ProductBasicAttributes


class Appliance(ProductBasicAttributes):
    def __init__(self, id, brand, type, display_name, price, inventory):
        super().__init__(id, brand, type, display_name, price, inventory, 'appliance')

    def reduce(self, quantity):
        self.inventory -= quantity
        self.update_inventory_status(self.inventory)
