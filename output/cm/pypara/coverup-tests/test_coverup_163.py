# file pypara/monetary.py:424-425
# lines [424, 425]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney

# Assuming Currency and Date are simple classes or namedtuples that can be instantiated
# Since the actual Currency and Date classes are not provided, we'll create mock classes for testing purposes
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
    # Setup if needed
    yield
    # Cleanup if needed

def test_some_money_as_boolean(cleanup):
    currency = MockCurrency('USD')
    date = MockDate(2023, 4, 1)
    
    # Test with non-zero quantity
    money_non_zero = SomeMoney(currency, Decimal('10.00'), date)
    assert money_non_zero.as_boolean() is True
    
    # Test with zero quantity
    money_zero = SomeMoney(currency, Decimal('0.00'), date)
    assert money_zero.as_boolean() is False
