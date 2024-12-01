from abc import ABC, abstractmethod


class MediatorEvent(ABC):
    @property
    @abstractmethod
    def EventName(self):
        pass


class StockReservationFailedEvent(MediatorEvent):
    def __init__(self, itemId: int, quantity: int):
        super().__init__()
        self.itemId = itemId
        self.quantity = quantity

    @property
    def EventName(self):
        return "StockReservationFailedEvent"


class PaymentFailedEvent(MediatorEvent):
    def __init__(self, clientId: int, storeId: int, amount: float):
        super().__init__()
        self.clientId = clientId
        self.storeId = storeId
        self.amount = amount

    @property
    def EventName(self):
        return "PaymentFailedEvent"


class ClientPurchaseSuccessfulEvent(MediatorEvent):
    def __init__(
        self, clientId: int, storeId: int, itemId: int, quantity: int, amout: float
    ):
        super().__init__()
        self.clientId = clientId
        self.storeId = storeId
        self.itemId = itemId
        self.quantity = quantity
        self.amout = amout

    @property
    def EventName(self):
        return "TransactionSuccessfulEvent"
