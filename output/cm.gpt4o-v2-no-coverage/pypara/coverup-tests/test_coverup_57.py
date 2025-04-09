# file: pypara/monetary.py:809-814
# asked: {"lines": [809, 810, 814], "branches": []}
# gained: {"lines": [809, 810, 814], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_abs_not_implemented():
    class TestPrice(Price):
        pass

    price = TestPrice()
    with pytest.raises(NotImplementedError):
        price.abs()
