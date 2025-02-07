# file: pypara/monetary.py:1240-1241
# asked: {"lines": [1240, 1241], "branches": []}
# gained: {"lines": [1240, 1241], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import Price, SomePrice

class TestSomePrice:
    def test_with_ccy(self):
        # Arrange
        original_ccy = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
        new_ccy = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
        qty = Decimal("100.00")
        dov = Date(2023, 1, 1)
        some_price = SomePrice(original_ccy, qty, dov)

        # Act
        new_price = some_price.with_ccy(new_ccy)

        # Assert
        assert new_price.ccy == new_ccy
        assert new_price.qty == qty
        assert new_price.dov == dov
        assert isinstance(new_price, SomePrice)
