# file pypara/monetary.py:1363-1364
# lines [1363, 1364]
# branches []

import pytest
from pypara.monetary import NonePrice, NoMoney

def test_none_price_times():
    none_price = NonePrice()
    result = none_price.times(5)
    assert isinstance(result, type(NoMoney)), "The result should be an instance of NoMoney"
