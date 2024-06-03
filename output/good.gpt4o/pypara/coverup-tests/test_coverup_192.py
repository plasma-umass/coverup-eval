# file pypara/monetary.py:468-471
# lines [470, 471]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Currency, Date

def test_scalar_add_executes_missing_lines():
    # Arrange
    currency = Currency('USD', '2', 2, 'standard', Decimal('0.01'), None)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date)
    other = 50  # This should be cast to Decimal inside the method

    # Act
    result = some_money.scalar_add(other)

    # Assert
    assert result.ccy == currency
    assert result.qty == (quantity + Decimal(other)).quantize(currency.quantizer)
    assert result.dov == date
