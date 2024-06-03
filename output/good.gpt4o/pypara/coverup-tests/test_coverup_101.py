# file pypara/monetary.py:424-425
# lines [424, 425]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Money, Currency
from typing import NamedTuple

class TestSomeMoney:
    def test_as_boolean(self):
        class SomeMoney(Money, NamedTuple("SomeMoney", [("ccy", Currency), ("qty", Decimal), ("dov", Date)])):
            def as_boolean(self) -> bool:
                return self[1].__bool__()

        currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
        quantity = Decimal("100.00")
        date_of_value = Date(2023, 1, 1)

        some_money = SomeMoney(currency, quantity, date_of_value)
        assert some_money.as_boolean() is True

        some_money_zero = SomeMoney(currency, Decimal("0.00"), date_of_value)
        assert some_money_zero.as_boolean() is False
