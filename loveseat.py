from furniture import Furniture


class Loveseat(Furniture):
    """
    Class to hold sofas data and methods
    """

    def __init__(self, id, brand, display_name, price, inventory):
        super().__init__(id, brand, 'Living Room', display_name, price, inventory)

    def __str__(self):
        return super().__str__()
