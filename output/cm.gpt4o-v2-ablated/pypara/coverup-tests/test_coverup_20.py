# file: pypara/monetary.py:650-651
# asked: {"lines": [650, 651], "branches": []}
# gained: {"lines": [650, 651], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_positive(self):
        none_money = NoneMoney()
        result = none_money.positive()
        assert result is none_money
