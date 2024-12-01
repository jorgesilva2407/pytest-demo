class ReservationFailedException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class PaymentFailedException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
