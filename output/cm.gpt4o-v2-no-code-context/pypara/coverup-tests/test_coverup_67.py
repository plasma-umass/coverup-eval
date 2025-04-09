# file: pypara/monetary.py:650-651
# asked: {"lines": [650, 651], "branches": []}
# gained: {"lines": [650], "branches": []}

import pytest
from pypara.monetary import Money

class TestNoneMoney:
    def test_positive_method(self):
        class NoneMoney(Money):
            def positive(self) -> "Money":
                return self

        none_money_instance = NoneMoney()
        result = none_money_instance.positive()
        
        assert result is none_money_instance
