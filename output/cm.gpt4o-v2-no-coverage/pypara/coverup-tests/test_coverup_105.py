# file: pypara/monetary.py:650-651
# asked: {"lines": [650, 651], "branches": []}
# gained: {"lines": [650, 651], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

def test_none_money_positive():
    none_money = NoneMoney()
    result = none_money.positive()
    assert result is none_money
