# file: pypara/monetary.py:1133-1135
# asked: {"lines": [1133, 1134, 1135], "branches": []}
# gained: {"lines": [1133, 1134, 1135], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

class TestSomePrice:
    def test_positive(self):
        # Arrange
        currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
        quantity = Decimal("100.00")
        date_of_value = Date(2023, 1, 1)
        some_price = SomePrice(currency, quantity, date_of_value)

        # Act
        positive_price = some_price.positive()

        # Assert
        assert positive_price.ccy == currency
        assert positive_price.qty == quantity
        assert positive_price.dov == date_of_value
        assert isinstance(positive_price, SomePrice)
