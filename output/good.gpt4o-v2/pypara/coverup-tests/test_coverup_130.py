# file: pypara/monetary.py:677-678
# asked: {"lines": [677, 678], "branches": []}
# gained: {"lines": [677, 678], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

def test_none_money_lte():
    none_money = NoneMoney()
    other_money = Money()  # Assuming Money can be instantiated like this

    assert none_money.lte(other_money) is True
