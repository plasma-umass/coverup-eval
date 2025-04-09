# file: pypara/monetary.py:689-690
# asked: {"lines": [689, 690], "branches": []}
# gained: {"lines": [689, 690], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_with_qty(self):
        none_money = NoneMoney()
        result = none_money.with_qty(Decimal('10.00'))
        assert result is none_money

    def test_with_qty_zero(self):
        none_money = NoneMoney()
        result = none_money.with_qty(Decimal('0.00'))
        assert result is none_money

    def test_with_qty_negative(self):
        none_money = NoneMoney()
        result = none_money.with_qty(Decimal('-10.00'))
        assert result is none_money
