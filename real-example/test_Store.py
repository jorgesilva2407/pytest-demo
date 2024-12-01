import pytest
from unittest.mock import MagicMock
from MediatorEvents import (
    PaymentFailedEvent,
    StockReservationFailedEvent,
    ClientPurchaseSuccessfulEvent,
)
from Mediator import Mediator
from Store import StockManager, PaymentGateway, Store
from ResultEnum import Result
from Constants import RESERVATION_FAILURE_CONSTANT_RETURN
from CustomExceptions import ReservationFailedException, PaymentFailedException


@pytest.fixture
def setup():
    stockManager = MagicMock(StockManager)
    paymentGateway = MagicMock(PaymentGateway)
    mediator = MagicMock(Mediator)
    store = Store(1, stockManager, paymentGateway, mediator)
    return stockManager, paymentGateway, mediator, store


class TestStore:
    def test_buy_shouldReturnSuccess_WhenAllOperationsSucceed(self, setup):
        stockManager, paymentGateway, _, store = setup
        stockManager.reserveItem.return_value = 100
        paymentGateway.charge.return_value = Result.SUCCESS

        result = store.buy(1, 1, 1)

        assert result == Result.SUCCESS

    def test_buy_shouldPublishClientPurchaseSuccessfulEvent_WhenAllOperationsSucceed(
        self, setup
    ):
        stockManager, paymentGateway, mediator, store = setup
        stockManager.reserveItem.return_value = 100
        paymentGateway.charge.return_value = Result.SUCCESS

        store.buy(1, 1, 1)

        mediator.publish.assert_called_once()
        event_type = mediator.publish.call_args[0][0]
        assert isinstance(event_type, ClientPurchaseSuccessfulEvent)

    def test_buy_shouldRaiseReservationFailedException_WhenStockManagerFails(
        self, setup
    ):
        stockManager, _, _, store = setup
        stockManager.reserveItem.return_value = (
            RESERVATION_FAILURE_CONSTANT_RETURN.value
        )

        with pytest.raises(ReservationFailedException):
            store.buy(1, 1, 1)

    def test_buy_shouldPublishStockReservationFailedEvent_WhenStockManagerFails(
        self, setup
    ):
        stockManager, _, mediator, store = setup
        stockManager.reserveItem.return_value = (
            RESERVATION_FAILURE_CONSTANT_RETURN.value
        )

        with pytest.raises(ReservationFailedException):
            store.buy(1, 1, 1)

        mediator.publish.assert_called_once()
        event_type = mediator.publish.call_args[0][0]
        assert isinstance(event_type, StockReservationFailedEvent)

    def test_buy_shouldRaisePaymentFailedException_WhenPaymentGatewayFails(self, setup):
        stockManager, paymentGateway, _, store = setup
        stockManager.reserveItem.return_value = 100
        paymentGateway.charge.return_value = Result.FAILURE

        with pytest.raises(PaymentFailedException):
            store.buy(1, 1, 1)

    def test_buy_shouldPublishPaymentFailedEvent_WhenPaymentGatewayFails(self, setup):
        stockManager, paymentGateway, mediator, store = setup
        stockManager.reserveItem.return_value = 100
        paymentGateway.charge.return_value = Result.FAILURE

        with pytest.raises(PaymentFailedException):
            store.buy(1, 1, 1)

        mediator.publish.assert_called_once()
        event_type = mediator.publish.call_args[0][0]
        assert isinstance(event_type, PaymentFailedEvent)
