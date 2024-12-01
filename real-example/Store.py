import random
from time import sleep
from Mediator import Mediator
from MediatorEvents import (
    StockReservationFailedEvent,
    PaymentFailedEvent,
    ClientPurchaseSuccessfulEvent,
)
from ResultEnum import Result
from Constants import RESERVATION_FAILURE_CONSTANT_RETURN
from CustomExceptions import ReservationFailedException, PaymentFailedException


class StockManager:
    def reserveItem(
        self,
        itemId: int,
        quantity: int,
    ) -> int:
        """
        This method simulates the reservation of an item in a stock.
        """
        sleep(600)
        isSuccess = random.choice([True, False])

        if isSuccess:
            return random.randint(1, 100) * quantity
        else:
            return RESERVATION_FAILURE_CONSTANT_RETURN.value


class PaymentGateway:
    def charge(
        self,
        fromId: int,
        toId: int,
        amount: float,
    ) -> Result:
        """
        This method simulates a payment between two bank accounts.
        """
        sleep(600)
        return random.choice([Result.SUCCESS, Result.FAILURE])


class Store:
    def __init__(
        self,
        bankAccountId: int,
        stockManager: StockManager,
        paymentGateway: PaymentGateway,
        mediator: Mediator,
    ):
        self._bankAccountId: int = bankAccountId
        self._stockManager: StockManager = stockManager
        self._paymentGateway: PaymentGateway = paymentGateway
        self._mediator: Mediator = mediator

    def buy(
        self,
        clientBankAccountId: int,
        itemId: int,
        quantity: int,
    ) -> Result:
        """
        This method simulates a purchase in a store.
        """
        amoutToPay = self._stockManager.reserveItem(itemId, quantity)
        if amoutToPay == RESERVATION_FAILURE_CONSTANT_RETURN.value:
            self._handleReservationFailed(itemId, quantity)

        paymentResult = self._paymentGateway.charge(
            clientBankAccountId,
            self._bankAccountId,
            amoutToPay,
        )
        if paymentResult == Result.FAILURE:
            self._handlePaymentFailed(clientBankAccountId, amoutToPay)

        return self._handleSuccessfulPurchase(
            clientBankAccountId,
            itemId,
            quantity,
            amoutToPay,
        )

    def _handleReservationFailed(
        self,
        itemId: int,
        quantity: int,
    ):
        self._mediator.publish(StockReservationFailedEvent(itemId, quantity))
        raise ReservationFailedException("Failed to reserve item")

    def _handlePaymentFailed(
        self,
        clientBankAccountId: int,
        amoutToPay: float,
    ):
        self._mediator.publish(
            PaymentFailedEvent(clientBankAccountId, self._bankAccountId, amoutToPay)
        )
        raise PaymentFailedException("Failed to charge")

    def _handleSuccessfulPurchase(
        self,
        clientBankAccountId: int,
        itemId: int,
        quantity: int,
        amoutToPay: float,
    ) -> Result:
        self._mediator.publish(
            ClientPurchaseSuccessfulEvent(
                clientBankAccountId, self._bankAccountId, itemId, quantity, amoutToPay
            )
        )
        return Result.SUCCESS
