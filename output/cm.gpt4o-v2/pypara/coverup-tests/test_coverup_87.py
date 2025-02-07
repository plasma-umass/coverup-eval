# file: pypara/monetary.py:1129-1131
# asked: {"lines": [1129, 1130, 1131], "branches": []}
# gained: {"lines": [1129, 1130, 1131], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_someprice_negative():
    # Arrange
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    quantity = Decimal("100.00")
    date_of_value = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, date_of_value)
    
    # Act
    negative_price = some_price.negative()
    
    # Assert
    assert negative_price.ccy == currency
    assert negative_price.qty == -quantity
    assert negative_price.dov == date_of_value
