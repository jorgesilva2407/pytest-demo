class Constant:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


RESERVATION_FAILURE_CONSTANT_RETURN = Constant(-1)
