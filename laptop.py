from electronics import Electronics

class Laptop(Electronics):
    """
    Class to hold Laptop data and methods
    """

    def __init__(self, id, brand, display_name, price, inventory, bluetooth, wifi, hdmi_output, ram_size):
        super().__init__(id, brand, 'Computer', display_name, price, inventory)
        self.bluetooth = bluetooth
        self.wifi = wifi
        self.hdmi_output = hdmi_output
        self.ram_size = ram_size

    def __str__(self):
        return super().__str__() + f', Bluetooth: {self.bluetooth}, WI-FI: {self.wifi}, HDMI Output: {self.hdmi_output}, RAM Size (GB): {self.ram_size}'
