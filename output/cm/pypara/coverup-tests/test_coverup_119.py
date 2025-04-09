# file pypara/monetary.py:1182-1185
# lines [1182, 1184, 1185]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, Price
from datetime import date

class MockCurrency(Currency):
    def __init__(self, code):
        super().__init__(code, 'Test Currency', 2, 'fiat', None, None)

@pytest.fixture
def mock_currency():
    return MockCurrency('USD')

def test_scalar_subtract(mock_currency):
    quantity = Decimal('100.00')
    dov = date.today()
    some_price = SomePrice(mock_currency, quantity, dov)

    # Subtract a numeric value that is not a Decimal
    other_value = 10  # An int, not a Decimal
    result = some_price.scalar_subtract(other_value)

    # Assertions to verify postconditions
    assert isinstance(result, Price), "The result should be a Price instance"
    assert result.ccy == mock_currency, "The currency should remain unchanged"
    assert result.qty == quantity - Decimal(other_value), "The quantity should be reduced by the value subtracted"
    assert result.dov == dov, "The date of value should remain unchanged"
