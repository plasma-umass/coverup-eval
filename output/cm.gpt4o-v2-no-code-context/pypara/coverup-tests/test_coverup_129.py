# file: pypara/monetary.py:1125-1127
# asked: {"lines": [1126, 1127], "branches": []}
# gained: {"lines": [1126, 1127], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Price, Currency, SomePrice

def test_someprice_abs():
    # Arrange
    currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    quantity = Decimal("-100.00")
    date_of_value = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, date_of_value)
    
    # Act
    abs_price = some_price.abs()
    
    # Assert
    assert abs_price.ccy == currency
    assert abs_price.qty == quantity.__abs__()
    assert abs_price.dov == date_of_value
