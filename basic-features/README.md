# Pytest Basic Features

- Automatically discover test files (files that begin with test_ or end with _test)
- Automatically discover tests (classes that begin with Test and functions that begin with test_)
- Run all tests in all subdirectories (pytest)
- Run single file or directory (pytest test_1_calculator.py)
- Fixtures for easy setup (@pytest.fixture)
- Parametrize for multiple identical calls (@pytest.parametrize)
- Markers (@pytest.mark) (pytest -m fast)
- Run all tests without a certain marker (pytest -k "not slow")
- Keywork find (pytest -k "add")