# file pypara/monetary.py:1119-1120
# lines [1120]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Currency, Price, SomePrice

def test_someprice_as_float():
    # Arrange
    currency = Currency("USD", "United States Dollar", 2, "fiat", Decimal("0.01"), None)
    quantity = Decimal("123.45")
    date_of_value = Date(2023, 1, 1)
    some_price = SomePrice(ccy=currency, qty=quantity, dov=date_of_value)
    
    # Act
    result = some_price.as_float()
    
    # Assert
    assert result == float(quantity)
