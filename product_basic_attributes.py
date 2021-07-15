class ProductBasicAttributes:

    def __init__(self, id, brand, type, display_name, price, inventory: int, category):
        self.id = id
        self.brand = brand
        self.type = type
        self.display_name = display_name
        self.price: float = price
        self.inventory = inventory
        self.inventory_status = inventory
        self.category = category
        self.warranty = category

    def __str__(self):
        return f'ID: {self.id}, Brand: {self.brand}, Type: {self.type}, Display Name: {self.display_name}, Price ($): {self.price}, Inventory: {self.inventory}, Inventory Status: {self.inventory_status}, Warranty (years): {self.warranty}'

    @property
    def inventory_status(self):
        return self.__inventory_status

    @inventory_status.setter
    def inventory_status(self, inventory):
        if inventory >= 10:
            self.__inventory_status = 'in stock'
        elif 0 < inventory < 10:
            self.__inventory_status = 'low stock'
        else:
            self.__inventory_status = 'out of stock'

    @property
    def warranty(self):
        return self.__warranty

    @warranty.setter
    def warranty(self, category):
        if category == 'furniture':
            self.__warranty = 2
        elif category == 'appliance':
            self.__warranty = 3
        elif category == 'electronics':
            self.__warranty = 1

    def replenish(self, amount):
        print(f"Inventory is lower than 5, replenishing now (+{amount})")
        self.inventory += amount
        self.update_inventory_status(self.inventory)

    def update_inventory_status(self, inventory):
        self.inventory_status = inventory
