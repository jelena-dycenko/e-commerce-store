from electronics import Electronics

class SmartTV(Electronics):
    """
    Class to hold Smart_TV data and methods
    """

    def __init__(self, id, brand, display_name, price, inventory, bluetooth, wifi, hdmi_input):
        super().__init__(id, brand, 'Television', display_name, price, inventory)
        self.bluetooth = bluetooth
        self.wifi = wifi
        self.hdmi_input = hdmi_input

    def __str__(self):
        return super().__str__() + f', Bluetooth: {self.bluetooth}, WI-FI: {self.wifi}, HDMI Input: {self.hdmi_input}'
