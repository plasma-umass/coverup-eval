# file: pypara/monetary.py:1116-1117
# asked: {"lines": [1117], "branches": []}
# gained: {"lines": [1117], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

class MockPrice:
    def __bool__(self):
        return True

def test_someprice_as_boolean():
    mock_currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    mock_qty = Decimal("100.00")
    mock_dov = Date(2023, 1, 1)
    
    some_price = SomePrice(ccy=mock_currency, qty=mock_qty, dov=mock_dov)
    
    assert some_price.as_boolean() is True

    mock_qty_zero = Decimal("0.00")
    some_price_zero = SomePrice(ccy=mock_currency, qty=mock_qty_zero, dov=mock_dov)
    
    assert some_price_zero.as_boolean() is False
