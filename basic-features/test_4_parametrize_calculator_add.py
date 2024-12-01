import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (1e100, 1e100, 2e100),
        (1e-100, 1e-100, 2e-100),
        (0.1, 0.2, 0.3),
    ],
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected
