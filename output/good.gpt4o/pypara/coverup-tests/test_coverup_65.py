# file pypara/monetary.py:1182-1185
# lines [1182, 1184, 1185]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Currency, Price, SomePrice

def test_someprice_scalar_subtract():
    # Arrange
    currency = Currency("USD", "United States Dollar", 2, Decimal('0.01'), None, None)
    quantity = Decimal("100.00")
    date_of_value = Date(2023, 1, 1)
    some_price = SomePrice(currency, quantity, date_of_value)
    
    # Act
    result = some_price.scalar_subtract(Decimal("10.00"))
    
    # Assert
    assert result.ccy == currency
    assert result.qty == Decimal("90.00")
    assert result.dov == date_of_value

    # Clean up
    del some_price
    del result
