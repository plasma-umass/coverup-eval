# file pypara/monetary.py:1246-1247
# lines [1246, 1247]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice

# Assuming Currency and Date are simple classes or namedtuples that can be instantiated
# Since the actual Currency and Date classes are not provided, we will mock them
class MockCurrency:
    def __init__(self, code):
        self.code = code

class MockDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_with_dov(cleanup):
    currency = MockCurrency('USD')
    quantity = Decimal('100.00')
    original_dov = MockDate(2023, 1, 1)
    new_dov = MockDate(2023, 1, 2)
    
    price = SomePrice(currency, quantity, original_dov)
    new_price = price.with_dov(new_dov)
    
    assert new_price.ccy == currency, "Currency should remain unchanged"
    assert new_price.qty == quantity, "Quantity should remain unchanged"
    assert new_price.dov == new_dov, "Date of value should be updated to the new value"
    assert new_price.dov != original_dov, "Date of value should not be the original value"
