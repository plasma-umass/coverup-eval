# file: pypara/monetary.py:680-681
# asked: {"lines": [680, 681], "branches": []}
# gained: {"lines": [680, 681], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

def test_none_money_gt():
    none_money = NoneMoney()
    other_money = NoneMoney()  # Using NoneMoney as the other instance of Money

    assert not none_money.gt(other_money)
