# file pypara/monetary.py:1159-1162
# lines [1161, 1162]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Currency, Price, SomePrice

def test_someprice_scalar_add():
    # Arrange
    currency = Currency("USD", "United States Dollar", 2, Decimal('0.01'), None, None)
    quantity = Decimal("100.00")
    date_of_value = Date(2023, 1, 1)
    some_price = SomePrice(currency, quantity, date_of_value)
    other_value = 50  # This should trigger the missing lines

    # Act
    result = some_price.scalar_add(other_value)

    # Assert
    assert result.ccy == currency
    assert result.qty == quantity + Decimal(other_value)
    assert result.dov == date_of_value
