# file pypara/monetary.py:491-494
# lines [493, 494]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Currency, Date

def test_scalar_subtract_executes_missing_lines():
    # Arrange
    currency = Currency('USD', 'US Dollar', 2, Decimal('0.01'), Decimal('0.01'), None)
    quantity = Decimal('100.00')
    date_of_value = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date_of_value)
    other_value = 10  # This should be cast to Decimal inside the method

    # Act
    result = some_money.scalar_subtract(other_value)

    # Assert
    assert isinstance(result, SomeMoney)
    assert result.ccy == currency
    assert result.qty == Decimal('90.00').quantize(currency.quantizer)
    assert result.dov == date_of_value
