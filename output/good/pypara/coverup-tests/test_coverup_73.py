# file pypara/monetary.py:698-700
# lines [698, 699, 700]
# branches []

import pytest
from pypara.monetary import NoneMoney, NoPrice

def test_none_money_price():
    none_money = NoneMoney()
    assert isinstance(none_money.price, NoPrice.__class__)
