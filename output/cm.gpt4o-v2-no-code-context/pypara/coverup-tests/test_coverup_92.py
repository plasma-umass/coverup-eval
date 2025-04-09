# file: pypara/monetary.py:674-675
# asked: {"lines": [674, 675], "branches": []}
# gained: {"lines": [674], "branches": []}

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def lt(self, other: "Money") -> bool:
        return other.defined

class TestNoneMoney:
    def test_lt_with_defined_other(self):
        class DefinedMoney(Money):
            @property
            def defined(self):
                return True

        none_money = NoneMoney()
        defined_money = DefinedMoney()
        
        assert none_money.lt(defined_money) is True

    def test_lt_with_undefined_other(self):
        class UndefinedMoney(Money):
            @property
            def defined(self):
                return False

        none_money = NoneMoney()
        undefined_money = UndefinedMoney()
        
        assert none_money.lt(undefined_money) is False
