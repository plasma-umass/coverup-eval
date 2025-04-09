# file pypara/monetary.py:441-443
# lines [441, 442, 443]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from typing import NamedTuple
from pypara.monetary import Money, Currency

class SomeMoney(Money, NamedTuple("SomeMoney", [("ccy", Currency), ("qty", Decimal), ("dov", Date)])):
    def positive(self) -> "Money":
        c, q, d = self
        return SomeMoney(c, q.__pos__(), d)

def test_some_money_positive():
    currency = Currency(code="USD", name="United States Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    quantity = Decimal("-100.00")
    date_of_value = Date(2023, 10, 1)
    
    some_money = SomeMoney(currency, quantity, date_of_value)
    positive_money = some_money.positive()
    
    assert positive_money.ccy == currency
    assert positive_money.qty == quantity.__pos__()
    assert positive_money.dov == date_of_value
