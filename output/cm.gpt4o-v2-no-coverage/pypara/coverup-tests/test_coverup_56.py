# file: pypara/monetary.py:698-700
# asked: {"lines": [698, 699, 700], "branches": []}
# gained: {"lines": [698, 699, 700], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Price, NoPrice

def test_none_money_price():
    none_money = NoneMoney()
    assert none_money.price is NoPrice
