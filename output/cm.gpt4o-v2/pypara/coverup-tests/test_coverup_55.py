# file: pypara/monetary.py:281-286
# asked: {"lines": [281, 282, 286], "branches": []}
# gained: {"lines": [281, 282], "branches": []}

import pytest
from pypara.monetary import Money
from pypara.currencies import Currency, CurrencyType
from decimal import Decimal

class ConcreteMoney(Money):
    def with_ccy(self, ccy: Currency) -> "Money":
        return self

def test_with_ccy():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    money = ConcreteMoney()
    result = money.with_ccy(ccy)
    assert result is money
