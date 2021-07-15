from furniture import Furniture


class Sofa(Furniture):
    """
    Class to hold sofas data and methods
    """

    def __init__(self, id, brand, display_name, price, inventory, color, height, width):
        super().__init__(id, brand, 'Living Room', display_name, price, inventory)
        self.color = color
        self.height = height
        self.width = width    # NOTE: use __<property> to not execute the setter on __init__

    def __str__(self):
        return super().__str__() + f', Color: {self.color}, Height (cm): {self.height}, Width (cm): {self.width}'