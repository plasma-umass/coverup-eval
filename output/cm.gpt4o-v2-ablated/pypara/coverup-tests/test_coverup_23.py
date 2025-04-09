# file: pypara/monetary.py:656-657
# asked: {"lines": [656, 657], "branches": []}
# gained: {"lines": [656, 657], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_scalar_add(self):
        none_money = NoneMoney()
        result = none_money.scalar_add(10)
        assert result is none_money
