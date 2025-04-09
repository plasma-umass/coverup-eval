# file pypara/monetary.py:1192-1194
# lines [1193, 1194]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, SomeMoney, Currency, Date

def test_someprice_times():
    # Arrange
    currency = Currency('USD', 'US Dollar', 2, Decimal('0.01'), Decimal('0.01'), None)
    quantity = Decimal('100.00')
    date_of_value = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, date_of_value)
    multiplier = Decimal('2.5')

    # Act
    result = some_price.times(multiplier)

    # Assert
    assert isinstance(result, SomeMoney)
    assert result.ccy == currency
    assert result.qty == (quantity * multiplier).quantize(currency.quantizer)
    assert result.dov == date_of_value
