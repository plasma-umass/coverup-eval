# file: pypara/monetary.py:647-648
# asked: {"lines": [647, 648], "branches": []}
# gained: {"lines": [647], "branches": []}

import pytest
from pypara.monetary import Money

class TestNoneMoney:
    def test_negative_method(self):
        class NoneMoney(Money):
            def negative(self) -> "Money":
                return self

        none_money_instance = NoneMoney()
        result = none_money_instance.negative()
        
        assert result is none_money_instance
