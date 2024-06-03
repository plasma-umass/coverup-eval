# file pypara/monetary.py:350-352
# lines [350, 351, 352]
# branches []

import pytest
from pypara.monetary import Money

def test_money_round_overload():
    class TestMoney(Money):
        def __round__(self) -> int:
            return 42

    money_instance = TestMoney()
    result = round(money_instance)
    assert result == 42
