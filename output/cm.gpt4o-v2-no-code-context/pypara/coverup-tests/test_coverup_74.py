# file: pypara/monetary.py:689-690
# asked: {"lines": [689, 690], "branches": []}
# gained: {"lines": [689], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Money

class NoneMoney(Money):
    def with_qty(self, qty: Decimal) -> "Money":
        return self

def test_none_money_with_qty():
    none_money = NoneMoney()
    result = none_money.with_qty(Decimal('10.00'))
    assert result is none_money
