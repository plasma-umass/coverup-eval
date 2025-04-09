# file: pypara/monetary.py:1137-1139
# asked: {"lines": [1137, 1138, 1139], "branches": []}
# gained: {"lines": [1137, 1138, 1139], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

class TestSomePrice:
    def test_round(self):
        # Setup
        currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
        quantity = Decimal("123.456")
        date_of_value = Date(2023, 1, 1)
        price = SomePrice(currency, quantity, date_of_value)

        # Exercise
        rounded_price = price.round(2)

        # Verify
        assert rounded_price.ccy == currency
        assert rounded_price.qty == Decimal("123.46")
        assert rounded_price.dov == date_of_value

    def test_round_no_digits(self):
        # Setup
        currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
        quantity = Decimal("123.456")
        date_of_value = Date(2023, 1, 1)
        price = SomePrice(currency, quantity, date_of_value)

        # Exercise
        rounded_price = price.round()

        # Verify
        assert rounded_price.ccy == currency
        assert rounded_price.qty == Decimal("123")
        assert rounded_price.dov == date_of_value
