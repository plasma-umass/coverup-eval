# file: pypara/monetary.py:698-700
# asked: {"lines": [698, 699, 700], "branches": []}
# gained: {"lines": [698, 699], "branches": []}

import pytest
from pypara.monetary import Money, NoPrice

def test_none_money_price():
    class NoneMoney(Money):
        @property
        def price(self) -> "Price":
            return NoPrice

    none_money_instance = NoneMoney()
    assert none_money_instance.price == NoPrice
