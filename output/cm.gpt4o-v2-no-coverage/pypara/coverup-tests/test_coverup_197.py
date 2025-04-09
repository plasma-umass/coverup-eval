# file: pypara/monetary.py:1122-1123
# asked: {"lines": [1123], "branches": []}
# gained: {"lines": [1123], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

@pytest.fixture
def some_price():
    ccy = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date.today()
    return SomePrice(ccy, qty, dov)

def test_as_integer(some_price):
    assert some_price.as_integer() == 100

def test_some_price_attributes(some_price):
    assert some_price.ccy.code == "USD"
    assert some_price.qty == Decimal("100.00")
    assert some_price.dov == Date.today()
