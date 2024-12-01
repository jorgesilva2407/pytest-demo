import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.fast
def test_add(calc):
    assert calc.add(1, 2) == 3


@pytest.mark.fast
def test_subtract(calc):
    assert calc.subtract(1, 2) == -1


@pytest.mark.fast
def test_multiply(calc):
    assert calc.multiply(1, 2) == 2


@pytest.mark.fast
def test_divide(calc):
    assert calc.divide(1, 2) == 0.5


@pytest.mark.slow
def test_slow_power(calc):
    assert calc.slow_power(2, int(1e10)) == 2 ** int(1e10)
