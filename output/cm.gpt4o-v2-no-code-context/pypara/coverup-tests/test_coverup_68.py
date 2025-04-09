# file: pypara/monetary.py:659-660
# asked: {"lines": [659, 660], "branches": []}
# gained: {"lines": [659], "branches": []}

import pytest
from pypara.monetary import Money

class TestNoneMoney:
    def test_subtract(self):
        class NoneMoney(Money):
            def subtract(self, other: "Money") -> "Money":
                return -other

        # Create a mock Money object
        class MockMoney(Money):
            def __neg__(self):
                return self

        none_money = NoneMoney()
        mock_money = MockMoney()

        result = none_money.subtract(mock_money)

        # Assert that the result is the negation of mock_money
        assert result is mock_money
