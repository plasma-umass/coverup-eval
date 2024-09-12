# file: pypara/monetary.py:635-636
# asked: {"lines": [635, 636], "branches": []}
# gained: {"lines": [635, 636], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_abs(self):
        none_money = NoneMoney()
        result = none_money.abs()
        assert result is none_money

    def test_abs_is_idempotent(self):
        none_money = NoneMoney()
        result1 = none_money.abs()
        result2 = result1.abs()
        assert result1 is result2
