# file: pypara/monetary.py:1125-1127
# asked: {"lines": [1125, 1126, 1127], "branches": []}
# gained: {"lines": [1125, 1126, 1127], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

class TestSomePrice:
    def test_abs(self):
        # Arrange
        ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
        qty = Decimal("-100.00")
        dov = Date(2023, 1, 1)
        price = SomePrice(ccy, qty, dov)

        # Act
        abs_price = price.abs()

        # Assert
        assert abs_price.ccy == ccy
        assert abs_price.qty == abs(qty)
        assert abs_price.dov == dov
