# file pypara/monetary.py:1125-1127
# lines [1125, 1126, 1127]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Price, Currency, SomePrice

def test_someprice_abs():
    # Arrange
    currency = Currency("USD", "United States Dollar", 2, Decimal('0.01'), None, None)
    quantity = Decimal("-100.00")
    dov = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, dov)
    
    # Act
    abs_price = some_price.abs()
    
    # Assert
    assert abs_price.ccy == currency
    assert abs_price.qty == abs(quantity)
    assert abs_price.dov == dov
