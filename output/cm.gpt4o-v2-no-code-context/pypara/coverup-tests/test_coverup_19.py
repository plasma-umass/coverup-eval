# file: pypara/monetary.py:1196-1202
# asked: {"lines": [1196, 1198, 1199, 1200, 1201, 1202], "branches": []}
# gained: {"lines": [1196, 1198, 1199, 1200, 1201, 1202], "branches": []}

import pytest
from decimal import Decimal, InvalidOperation, DivisionByZero
from pypara.monetary import SomePrice, NoPrice, Currency, Date

@pytest.fixture
def some_price():
    currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    return SomePrice(currency, Decimal("100.00"), Date(2023, 10, 1))

def test_divide_valid(some_price):
    result = some_price.divide(2)
    assert result == SomePrice(some_price.ccy, Decimal("50.00"), some_price.dov)

def test_divide_invalid_operation(some_price):
    result = some_price.divide("invalid")
    assert result == NoPrice

def test_divide_by_zero(some_price):
    result = some_price.divide(0)
    assert result == NoPrice

def test_divide_invalid_type(some_price):
    with pytest.raises(TypeError):
        some_price.divide(None)
