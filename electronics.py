from product_basic_attributes import ProductBasicAttributes


class Electronics(ProductBasicAttributes):
    def __init__(self, id, brand, type, display_name, price, inventory):
        super().__init__(id, brand, type, display_name, price, inventory, 'electronics')

    def reduce(self, quantity):
        self.inventory -= quantity
        self.update_inventory_status(self.inventory)
