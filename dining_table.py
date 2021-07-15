from furniture import Furniture

class DiningTable(Furniture):
    """
    Class to hold Dining_Tables data and methods
    """

    def __init__(self, id, brand, display_name, price, inventory, made_in, material):
        super().__init__(id, brand, 'Dining Room', display_name, price, inventory)
        self.made_in = made_in
        self.material = material

    def __str__(self):
        return super().__str__() + f', Made in : {self.made_in}, Material: {self.material}'