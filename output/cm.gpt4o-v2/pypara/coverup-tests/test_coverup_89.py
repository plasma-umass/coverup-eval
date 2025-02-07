# file: pypara/monetary.py:1125-1127
# asked: {"lines": [1125, 1126, 1127], "branches": []}
# gained: {"lines": [1125, 1126, 1127], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import Price, SomePrice

class TestSomePrice:
    
    def test_abs_method(self):
        # Arrange
        currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
        quantity = Decimal('-123.45')
        date_of_value = Date(2023, 1, 1)
        some_price = SomePrice(currency, quantity, date_of_value)
        
        # Act
        abs_price = some_price.abs()
        
        # Assert
        assert abs_price.ccy == currency
        assert abs_price.qty == abs(quantity)
        assert abs_price.dov == date_of_value
