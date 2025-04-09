# file pypara/monetary.py:1187-1190
# lines [1187, 1189, 1190]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from collections import namedtuple

# Assuming Currency and Price are defined somewhere in pypara.monetary
from pypara.monetary import Currency, Price

# Mocking the necessary classes for the test
class MockCurrency(Currency):
    def __init__(self):
        super().__init__(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal('0.01'), hashcache=None)

class MockPrice(Price):
    pass

# The class under test
class SomePrice(MockPrice, namedtuple("SomePrice", ["ccy", "qty", "dov"])):
    ccy: MockCurrency
    qty: Decimal
    dov: Date

    def multiply(self, other: Decimal) -> "SomePrice":
        c, q, d = self
        return SomePrice(c, q * Decimal(other), d)

@pytest.fixture
def some_price():
    return SomePrice(MockCurrency(), Decimal('10.0'), Date(2023, 1, 1))

def test_some_price_multiply(some_price):
    result = some_price.multiply(2)
    assert result.qty == Decimal('20.0')
    assert result.ccy == some_price.ccy
    assert result.dov == some_price.dov
