# file pypara/monetary.py:1363-1364
# lines [1363, 1364]
# branches []

import pytest
from pypara.monetary import Price, NoMoney, Money

class NonePrice(Price):
    def times(self, other: "Numeric") -> Money:
        return NoMoney

class TestNonePrice:
    def test_times_returns_no_money(self):
        none_price = NonePrice()
        result = none_price.times(10)
        assert result == NoMoney
