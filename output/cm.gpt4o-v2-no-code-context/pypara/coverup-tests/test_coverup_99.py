# file: pypara/monetary.py:427-428
# asked: {"lines": [427, 428], "branches": []}
# gained: {"lines": [427], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from collections import namedtuple
from pypara.monetary import Money, Currency

class TestSomeMoney:
    def test_as_float(self):
        SomeMoney = namedtuple("SomeMoney", ["ccy", "qty", "dov"])
        
        class SomeMoneyClass(Money, SomeMoney):
            def as_float(self) -> float:
                return self[1].__float__()

        currency = Currency("USD", "United States Dollar", 2, "fiat", Decimal("0.01"), None)
        quantity = Decimal("123.45")
        date_of_value = Date(2023, 10, 1)
        some_money = SomeMoneyClass(currency, quantity, date_of_value)

        result = some_money.as_float()
        assert result == float(quantity)
