# file pypara/monetary.py:1137-1139
# lines [1137, 1138, 1139]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice

# Assuming Currency and Date are simple classes or namedtuples that can be instantiated
# As the actual implementation of Currency and Date is not provided, we will mock these classes
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
    # Setup if necessary
    yield
    # Cleanup code if necessary

def test_some_price_round(cleanup):
    currency = MockCurrency('USD')
    quantity = Decimal('123.456')
    date_of_value = MockDate(2023, 4, 1)
    some_price = SomePrice(currency, quantity, date_of_value)

    # Round the quantity to 0 decimal places
    rounded_price = some_price.round(0)
    assert rounded_price.qty == Decimal('123')

    # Round the quantity to 2 decimal places
    rounded_price = some_price.round(2)
    assert rounded_price.qty == Decimal('123.46')

    # Ensure the currency and date_of_value remain unchanged
    assert rounded_price.ccy == currency
    assert rounded_price.dov == date_of_value
