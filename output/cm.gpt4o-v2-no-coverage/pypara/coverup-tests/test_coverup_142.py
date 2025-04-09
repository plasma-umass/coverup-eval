# file: pypara/monetary.py:1363-1364
# asked: {"lines": [1363, 1364], "branches": []}
# gained: {"lines": [1363, 1364], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NonePrice
from pypara.commons.numbers import Numeric
from pypara.monetary import NoMoney

class MockPrice:
    def times(self, other: Numeric):
        return NoMoney

def test_none_price_times():
    none_price = NonePrice()
    result = none_price.times(Decimal('10.0'))
    assert result == NoMoney
