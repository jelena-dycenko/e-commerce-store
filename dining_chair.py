from furniture import Furniture

class DiningChair(Furniture):
    """
    Class to hold Dining_Chairs data and methods
    """

    def __init__(self, id, brand, display_name, price, inventory):
        super().__init__(id, brand, 'Dining Room', display_name, price, inventory)

    def __str__(self):
        return super().__str__()