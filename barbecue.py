from appliance import Appliance

class Barbecue(Appliance):
    """
    Class to hold Barbecues data and methods
    """

    def __init__(self, id, brand, display_name, price, inventory):
        super().__init__(id, brand, 'Cooking', display_name, price, inventory)

    def __str__(self):
        return super().__str__()