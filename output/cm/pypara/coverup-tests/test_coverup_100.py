# file pypara/monetary.py:437-439
# lines [437, 438, 439]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomeMoney

# Assuming Currency is a namedtuple or class that requires specific arguments
# For the purpose of this test, we will mock the Currency class
class MockCurrency:
    def __init__(self, name, decimals=None, type=None, quantizer=None, hashcache=None):
        self.name = name
        self.decimals = decimals
        self.type = type
        self.quantizer = quantizer
        self.hashcache = hashcache

@pytest.fixture
def cleanup():
    # Setup code if needed
    yield
    # Cleanup code if needed

def test_some_money_negative(cleanup, mocker):
    mocker.patch('pypara.monetary.Currency', MockCurrency)
    currency = MockCurrency('USD')
    quantity = Decimal('100.00')
    dov = date.today()
    money = SomeMoney(currency, quantity, dov)

    negative_money = money.negative()

    assert negative_money.ccy == currency
    assert negative_money.qty == -quantity
    assert negative_money.dov == dov
