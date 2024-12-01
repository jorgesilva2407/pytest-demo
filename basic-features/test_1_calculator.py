from calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3


def test_subtract():
    calc = Calculator()
    assert calc.subtract(1, 2) == -1


def test_multiply():
    calc = Calculator()
    assert calc.multiply(1, 2) == 2


def test_divide():
    calc = Calculator()
    assert calc.divide(1, 2) == 0.5


def test_slow_power():
    calc = Calculator()
    assert calc.slow_power(2, 3) == 8
