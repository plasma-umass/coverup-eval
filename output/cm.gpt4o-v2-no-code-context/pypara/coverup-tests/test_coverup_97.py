# file: pypara/monetary.py:1363-1364
# asked: {"lines": [1363, 1364], "branches": []}
# gained: {"lines": [1363, 1364], "branches": []}

import pytest
from pypara.monetary import NonePrice, NoMoney, Money

def test_none_price_times():
    none_price = NonePrice()
    result = none_price.times(10)
    assert result == NoMoney
