# file pypara/monetary.py:421-422
# lines [421, 422]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from typing import NamedTuple, Any
from pypara.monetary import Money, Currency

class TestSomeMoney:
    def test_is_equal(self):
        class SomeMoney(Money, NamedTuple("SomeMoney", [("ccy", Currency), ("qty", Decimal), ("dov", Date)])):
            def is_equal(self, other: Any) -> bool:
                return other.__class__ is SomeMoney and tuple(self) == tuple(other)

        currency = Currency(code="USD", name="United States Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
        some_money1 = SomeMoney(ccy=currency, qty=Decimal("100.00"), dov=Date(2023, 1, 1))
        some_money2 = SomeMoney(ccy=currency, qty=Decimal("100.00"), dov=Date(2023, 1, 1))
        some_money3 = SomeMoney(ccy=currency, qty=Decimal("200.00"), dov=Date(2023, 1, 1))

        assert some_money1.is_equal(some_money2) is True
        assert some_money1.is_equal(some_money3) is False
        assert some_money1.is_equal("not a SomeMoney instance") is False
