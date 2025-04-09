# file: pypara/monetary.py:692-693
# asked: {"lines": [692, 693], "branches": []}
# gained: {"lines": [692], "branches": []}

import pytest
from pypara.monetary import Money

class TestNoneMoney:
    def test_with_dov(self):
        class NoneMoney(Money):
            def with_dov(self, dov) -> "Money":
                return self

        none_money = NoneMoney()
        result = none_money.with_dov(dov="2023-10-01")
        assert result is none_money
