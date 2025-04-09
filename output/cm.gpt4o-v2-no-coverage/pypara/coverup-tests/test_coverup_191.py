# file: pypara/monetary.py:1054-1055
# asked: {"lines": [1055], "branches": []}
# gained: {"lines": [1055], "branches": []}

import pytest
from pypara.monetary import Price

class TestPrice(Price):
    def round(self, ndigits: int = 0) -> 'Price':
        # Simple implementation for testing purposes
        return self

    def __hash__(self):
        # Implementing __hash__ to avoid unhashable type error
        return hash(id(self))

@pytest.fixture
def price():
    return TestPrice()

def test_price_rounding(price):
    # Test rounding with default ndigits
    rounded_price = round(price)
    assert isinstance(rounded_price, Price)
    
    # Test rounding with specific ndigits
    rounded_price = round(price, 2)
    assert isinstance(rounded_price, Price)
    
    # Test rounding with ndigits as None
    rounded_price = round(price, None)
    assert isinstance(rounded_price, Price)
