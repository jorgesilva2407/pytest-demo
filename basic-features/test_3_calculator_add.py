import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(1, 2) == 3


def test_add_big_numbers(calc):
    assert calc.add(1e100, 1e100) == 2e100


def test_add_small_numbers(calc):
    assert calc.add(1e-100, 1e-100) == 2e-100


def test_add_floats(calc):
    assert calc.add(0.1, 0.2) == 0.3
