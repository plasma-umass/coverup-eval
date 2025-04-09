# file: pypara/monetary.py:1182-1185
# asked: {"lines": [1182, 1184, 1185], "branches": []}
# gained: {"lines": [1182, 1184, 1185], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, Date

@pytest.fixture
def currency():
    return Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)

@pytest.fixture
def date_of_value():
    return Date(2023, 10, 1)

def test_scalar_subtract(currency, date_of_value):
    # Arrange
    quantity = Decimal("100.00")
    price = SomePrice(currency, quantity, date_of_value)
    other = Decimal("10.00")

    # Act
    result = price.scalar_subtract(other)

    # Assert
    assert result.ccy == currency
    assert result.qty == quantity - other
    assert result.dov == date_of_value

def test_scalar_subtract_with_int(currency, date_of_value):
    # Arrange
    quantity = Decimal("100.00")
    price = SomePrice(currency, quantity, date_of_value)
    other = 10  # integer value

    # Act
    result = price.scalar_subtract(other)

    # Assert
    assert result.ccy == currency
    assert result.qty == quantity - Decimal(other)
    assert result.dov == date_of_value

def test_scalar_subtract_with_float(currency, date_of_value):
    # Arrange
    quantity = Decimal("100.00")
    price = SomePrice(currency, quantity, date_of_value)
    other = 10.5  # float value

    # Act
    result = price.scalar_subtract(other)

    # Assert
    assert result.ccy == currency
    assert result.qty == quantity - Decimal(str(other))
    assert result.dov == date_of_value
