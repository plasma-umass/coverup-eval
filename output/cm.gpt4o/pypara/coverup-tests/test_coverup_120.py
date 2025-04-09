# file pypara/monetary.py:1390-1391
# lines [1390, 1391]
# branches []

import pytest
from pypara.monetary import Price
from datetime import date as Date

class TestNonePrice:
    def test_with_dov(self):
        class NonePrice(Price):
            def with_dov(self, dov: Date) -> "Price":
                return self

        none_price = NonePrice()
        result = none_price.with_dov(Date.today())
        assert result is none_price
