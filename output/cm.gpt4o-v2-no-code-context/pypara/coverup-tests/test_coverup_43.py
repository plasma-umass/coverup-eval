# file: pypara/monetary.py:1042-1044
# asked: {"lines": [1042, 1043, 1044], "branches": []}
# gained: {"lines": [1042, 1043], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_round_int():
    class TestPrice(Price):
        def __round__(self) -> int:
            return 42

    price = TestPrice()
    result = round(price)
    assert result == 42

