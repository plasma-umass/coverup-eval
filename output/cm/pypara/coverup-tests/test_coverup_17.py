# file pypara/monetary.py:1226-1231
# lines [1226, 1227, 1228, 1229, 1230, 1231]
# branches ['1227->1228', '1227->1229', '1229->1230', '1229->1231']

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice, Price, IncompatibleCurrencyError

class MockCurrency:
    def __init__(self, code):
        self.code = code

    def __eq__(self, other):
        return self.code == other.code

@pytest.fixture
def some_price():
    return SomePrice(MockCurrency('USD'), Decimal('100.00'), date.today())

@pytest.fixture
def other_price():
    return SomePrice(MockCurrency('EUR'), Decimal('90.00'), date.today())

@pytest.fixture
def undefined_price():
    class UndefinedPrice(Price):
        @property
        def undefined(self):
            return True

    return UndefinedPrice()

def test_some_price_greater_than_undefined_price(some_price, undefined_price):
    assert some_price.gt(undefined_price) is True

def test_some_price_greater_than_other_price_with_different_currency(some_price, other_price):
    with pytest.raises(IncompatibleCurrencyError) as exc_info:
        some_price.gt(other_price)
    assert exc_info.value.ccy1 == some_price.ccy
    assert exc_info.value.ccy2 == other_price.ccy
    assert 'comparision' in exc_info.value.operation

def test_some_price_greater_than_other_price_with_same_currency(some_price):
    other_price_same_currency = SomePrice(MockCurrency('USD'), Decimal('80.00'), date.today())
    assert some_price.gt(other_price_same_currency) is True
