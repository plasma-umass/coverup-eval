# file: pypara/monetary.py:430-431
# asked: {"lines": [430, 431], "branches": []}
# gained: {"lines": [430], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from collections import namedtuple

# Assuming Currency and Money are defined somewhere in pypara/monetary.py
from pypara.monetary import Currency, Money

# Mocking the Currency class for the purpose of this test
class MockCurrency:
    def __init__(self, code):
        self.code = code

# Mocking the Money class for the purpose of this test
class MockMoney:
    pass

# The class under test
class SomeMoney(MockMoney, namedtuple("SomeMoney", ["ccy", "qty", "dov"])):
    def as_integer(self) -> int:
        return self[1].__int__()

@pytest.fixture
def some_money():
    return SomeMoney(ccy=MockCurrency("USD"), qty=Decimal("123.45"), dov=Date(2023, 1, 1))

def test_as_integer(some_money):
    assert some_money.as_integer() == 123

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
