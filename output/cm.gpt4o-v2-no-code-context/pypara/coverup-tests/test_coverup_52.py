# file: pypara/monetary.py:1187-1190
# asked: {"lines": [1187, 1189, 1190], "branches": []}
# gained: {"lines": [1187, 1189, 1190], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, Date

def test_someprice_multiply():
    # Arrange
    currency = Currency("USD", "United States Dollar", 2, "fiat", Decimal("0.01"), None)
    quantity = Decimal("100.00")
    date_of_value = Date(2023, 10, 1)
    price = SomePrice(currency, quantity, date_of_value)
    multiplier = 2

    # Act
    result = price.multiply(multiplier)

    # Assert
    assert result.ccy == currency
    assert result.qty == quantity * Decimal(multiplier)
    assert result.dov == date_of_value

    # Clean up
    del price
    del result
