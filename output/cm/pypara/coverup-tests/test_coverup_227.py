# file pypara/monetary.py:830-836
# lines [836]
# branches []

import pytest
from pypara.monetary import Price

class TestPrice(Price):
    def __init__(self, amount):
        self.amount = amount

    def round(self, ndigits: int = 0) -> "Price":
        return super().round(ndigits)

@pytest.fixture
def test_price():
    return TestPrice(amount=0)

def test_price_round_not_implemented_error(test_price):
    with pytest.raises(NotImplementedError):
        test_price.round()
