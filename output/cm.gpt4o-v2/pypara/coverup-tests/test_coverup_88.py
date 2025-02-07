# file: pypara/monetary.py:1159-1162
# asked: {"lines": [1159, 1161, 1162], "branches": []}
# gained: {"lines": [1159, 1161, 1162], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_scalar_add():
    # Arrange
    currency = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    price = SomePrice(currency, quantity, date)
    add_value = 50

    # Act
    result = price.scalar_add(add_value)

    # Assert
    assert result.ccy == currency
    assert result.qty == quantity + Decimal(add_value)
    assert result.dov == date

    # Clean up
    del price
    del result
