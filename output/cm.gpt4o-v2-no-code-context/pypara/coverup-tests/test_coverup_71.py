# file: pypara/monetary.py:683-684
# asked: {"lines": [683, 684], "branches": []}
# gained: {"lines": [683], "branches": []}

import pytest
from pypara.monetary import Money

class TestNoneMoney:
    def test_gte_with_undefined_other(self):
        class NoneMoney(Money):
            def gte(self, other: "Money") -> bool:
                return other.undefined

        class MockMoney:
            def __init__(self, undefined):
                self.undefined = undefined

        none_money = NoneMoney()
        other_money = MockMoney(undefined=True)
        
        assert none_money.gte(other_money) is True

        other_money = MockMoney(undefined=False)
        
        assert none_money.gte(other_money) is False
