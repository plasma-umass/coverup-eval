# file pypara/monetary.py:1125-1127
# lines [1125, 1126, 1127]
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

def test_someprice_abs(cleanup):
    currency = MockCurrency('USD')
    quantity = Decimal('-123.45')
    dov = date.today()
    price = SomePrice(currency, quantity, dov)
    
    abs_price = price.abs()
    
    assert abs_price.ccy == currency, "Currency should remain the same after taking absolute value"
    assert abs_price.qty == abs(quantity), "Quantity should be the absolute value of the original quantity"
    assert abs_price.dov == dov, "Date of value should remain the same after taking absolute value"
