# file: pypara/monetary.py:665-666
# asked: {"lines": [665, 666], "branches": []}
# gained: {"lines": [665], "branches": []}

import pytest
from pypara.monetary import Money

class TestNoneMoney:
    def test_multiply(self):
        class NoneMoney(Money):
            def multiply(self, other) -> "Money":
                return self

        none_money = NoneMoney()
        result = none_money.multiply(10)
        assert result is none_money
