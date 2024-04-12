# file pypara/monetary.py:1187-1190
# lines [1187, 1189, 1190]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice

class MockCurrency:
    def __init__(self, code):
        self.code = code

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_someprice_multiply(cleanup):
    currency = MockCurrency('USD')
    quantity = Decimal('100.00')
    dov = date.today()
    some_price = SomePrice(currency, quantity, dov)

    multiplier = 2
    expected_quantity = quantity * Decimal(multiplier)
    result = some_price.multiply(multiplier)

    assert result.ccy == currency, "Currency should remain unchanged after multiplication."
    assert result.qty == expected_quantity, "Quantity should be correctly multiplied."
    assert result.dov == dov, "Date of value should remain unchanged after multiplication."
