# file: pypara/monetary.py:1243-1244
# asked: {"lines": [1243, 1244], "branches": []}
# gained: {"lines": [1243, 1244], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

class TestSomePrice:
    def test_with_qty(self):
        # Arrange
        currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
        original_qty = Decimal("100.00")
        new_qty = Decimal("200.00")
        dov = Date.today()
        price = SomePrice(currency, original_qty, dov)

        # Act
        new_price = price.with_qty(new_qty)

        # Assert
        assert new_price.qty == new_qty
        assert new_price.ccy == price.ccy
        assert new_price.dov == price.dov
        assert new_price != price
