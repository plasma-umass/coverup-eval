# file pypara/monetary.py:1119-1120
# lines [1119, 1120]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Currency, Price
from typing import NamedTuple

class TestSomePrice:
    def test_as_float(self):
        class SomePrice(Price, NamedTuple("SomePrice", [("ccy", Currency), ("qty", Decimal), ("dov", Date)])):
            def as_float(self) -> float:
                return self.qty.__float__()

        currency = Currency(
            code="USD",
            name="United States Dollar",
            decimals=2,
            type="fiat",
            quantizer=Decimal("0.01"),
            hashcache=None
        )
        quantity = Decimal("123.45")
        date_of_value = Date(2023, 10, 1)
        some_price = SomePrice(ccy=currency, qty=quantity, dov=date_of_value)

        assert some_price.as_float() == float(quantity)
