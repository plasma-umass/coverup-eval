# file: pypara/monetary.py:1122-1123
# asked: {"lines": [1122, 1123], "branches": []}
# gained: {"lines": [1122, 1123], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_someprice_as_integer():
    # Arrange
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    quantity = Decimal('123.45')
    date_of_value = Date(2023, 10, 5)
    some_price = SomePrice(ccy=currency, qty=quantity, dov=date_of_value)
    
    # Act
    result = some_price.as_integer()
    
    # Assert
    assert result == 123

