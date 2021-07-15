from appliance import Appliance

class TopFreezer(Appliance):
    """
    Class to hold Top_Freezer data and methods
    """

    def __init__(self, id, brand, display_name, price, inventory, drawers, door_color, capacity):
        super().__init__(id, brand, 'Refrigerators', display_name, price, inventory)
        self.drawers = drawers
        self.door_color = door_color
        self.capacity = capacity

    def __str__(self):
        return super().__str__() + f', Drawers: {self.drawers}, Door Color: {self.door_color}, Capacity (m^3): {self.capacity}'