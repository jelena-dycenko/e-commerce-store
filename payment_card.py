class PaymentCard:
    """
    Class to hold PaymentCard data and methods
    """

    def __init__(self, num: str, expiry_date: str, holder_name: str, balance: float):
        self.num = num
        self.expiry_date = expiry_date
        self.holder_name = holder_name
        self.balance = balance