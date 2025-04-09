# file: pypara/monetary.py:680-681
# asked: {"lines": [680, 681], "branches": []}
# gained: {"lines": [680, 681], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

def test_none_money_gt():
    none_money = NoneMoney()
    other_money = Money()  # Assuming Money can be instantiated like this

    assert none_money.gt(other_money) == False
