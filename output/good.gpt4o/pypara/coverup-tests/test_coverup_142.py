# file pypara/monetary.py:1187-1190
# lines [1189, 1190]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Price, Currency, SomePrice

def test_someprice_multiply():
    # Arrange
    currency = Currency("USD", "United States Dollar", 2, "fiat", Decimal("0.01"), None)
    quantity = Decimal("100.00")
    date_of_value = Date(2023, 1, 1)
    some_price = SomePrice(currency, quantity, date_of_value)
    multiplier = 2

    # Act
    result = some_price.multiply(multiplier)

    # Assert
    assert result.ccy == currency
    assert result.qty == quantity * Decimal(multiplier)
    assert result.dov == date_of_value
