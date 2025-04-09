# file: pypara/monetary.py:1348-1349
# asked: {"lines": [1348, 1349], "branches": []}
# gained: {"lines": [1348, 1349], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class MockPrice(Price):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, MockPrice) and self.value == other.value

def test_none_price_add():
    none_price = NonePrice()
    other_price = MockPrice(100)

    result = none_price.add(other_price)

    assert result == other_price

@pytest.fixture(autouse=True)
def cleanup():
    # Add any necessary cleanup code here
    yield
    # Cleanup code to ensure no state pollution
