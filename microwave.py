from appliance import Appliance


class Microwave(Appliance):
    """
    Class to hold Microwaves data and methods
    """

    def __init__(self, id, brand, display_name, price, inventory, depth):
        super().__init__(id, brand, 'Cooking', display_name, price, inventory)
        self.depth = depth

    def __str__(self):
        return super().__str__() + f', Depth (cm): {self.depth}'