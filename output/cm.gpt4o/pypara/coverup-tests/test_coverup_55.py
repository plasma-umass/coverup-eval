# file pypara/monetary.py:433-435
# lines [433, 434, 435]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from typing import NamedTuple
from pypara.monetary import Money, Currency

class SomeMoney(Money, NamedTuple("SomeMoney", [("ccy", Currency), ("qty", Decimal), ("dov", Date)])):
    def abs(self) -> "Money":
        c, q, d = self
        return SomeMoney(c, q.__abs__(), d)

def test_somemoney_abs():
    currency = Currency(
        code="USD",
        name="United States Dollar",
        decimals=2,
        type="fiat",
        quantizer=Decimal("0.01"),
        hashcache=None
    )
    quantity = Decimal("-100.00")
    date_of_value = Date(2023, 1, 1)
    
    some_money = SomeMoney(currency, quantity, date_of_value)
    abs_money = some_money.abs()
    
    assert abs_money.ccy == currency
    assert abs_money.qty == quantity.__abs__()
    assert abs_money.dov == date_of_value
