# file pypara/monetary.py:1246-1247
# lines [1246, 1247]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from typing import NamedTuple
from pypara.monetary import Price, Currency

class TestSomePrice:
    def test_with_dov(self):
        class SomePrice(Price, NamedTuple("SomePrice", [("ccy", Currency), ("qty", Decimal), ("dov", Date)])):
            def with_dov(self, dov: Date) -> "Price":
                return SomePrice(self[0], self[1], dov)

        currency = Currency(code="USD", name="United States Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
        quantity = Decimal("100.00")
        original_dov = Date(2023, 1, 1)
        new_dov = Date(2023, 12, 31)

        some_price = SomePrice(currency, quantity, original_dov)
        updated_price = some_price.with_dov(new_dov)

        assert updated_price.ccy == currency
        assert updated_price.qty == quantity
        assert updated_price.dov == new_dov
        assert updated_price.dov != original_dov
