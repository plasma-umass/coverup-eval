# file pypara/monetary.py:1102-1112
# lines [1102, 1103, 1107, 1109, 1111]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice

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

def test_some_price_defined_and_undefined(cleanup):
    currency = MockCurrency('USD')
    quantity = Decimal('100.00')
    date_of_value = MockDate(2023, 1, 1)
    price = SomePrice(ccy=currency, qty=quantity, dov=date_of_value)

    assert price.defined is True
    assert price.undefined is False
    assert price.ccy == currency
    assert price.qty == quantity
    assert price.dov == date_of_value
