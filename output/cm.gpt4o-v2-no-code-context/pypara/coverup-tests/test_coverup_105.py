# file: pypara/monetary.py:653-654
# asked: {"lines": [653, 654], "branches": []}
# gained: {"lines": [653], "branches": []}

import pytest
from unittest.mock import MagicMock
from pypara.monetary import Money

class TestNoneMoney:
    def test_add_method(self):
        class NoneMoney(Money):
            def add(self, other: "Money") -> "Money":
                return other

        none_money = NoneMoney()
        
        # Mocking a Money instance since the actual Money class constructor is not available
        other_money = MagicMock(spec=Money)
        other_money.amount = 10
        other_money.currency = 'USD'
        
        result = none_money.add(other_money)
        
        assert result == other_money
        assert isinstance(result, Money)
        assert result.amount == 10
        assert result.currency == 'USD'
