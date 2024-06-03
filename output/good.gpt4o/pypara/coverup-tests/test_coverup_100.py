# file pypara/monetary.py:1345-1346
# lines [1345, 1346]
# branches []

import pytest
from pypara.monetary import Price

class NonePrice(Price):
    def positive(self) -> "Price":
        return self

def test_none_price_positive():
    none_price = NonePrice()
    result = none_price.positive()
    assert result is none_price
