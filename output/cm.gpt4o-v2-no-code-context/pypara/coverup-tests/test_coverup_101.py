# file: pypara/monetary.py:1387-1388
# asked: {"lines": [1387, 1388], "branches": []}
# gained: {"lines": [1387], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Price

class TestNonePrice:
    def test_with_qty(self):
        class NonePrice(Price):
            def with_qty(self, qty: Decimal) -> "Price":
                return self

        none_price = NonePrice()
        result = none_price.with_qty(Decimal('10.00'))
        assert result is none_price
