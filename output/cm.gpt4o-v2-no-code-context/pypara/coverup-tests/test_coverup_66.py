# file: pypara/monetary.py:644-645
# asked: {"lines": [644, 645], "branches": []}
# gained: {"lines": [644], "branches": []}

import pytest
from pypara.monetary import Money

class TestNoneMoney:
    def test_round_method(self):
        class NoneMoney(Money):
            def round(self, ndigits: int = 0) -> "Money":
                return self

        none_money = NoneMoney()
        result = none_money.round(2)
        assert result is none_money
