# file: pypara/monetary.py:1133-1135
# asked: {"lines": [1133, 1134, 1135], "branches": []}
# gained: {"lines": [1133, 1134, 1135], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_someprice_positive():
    # Arrange
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    quantity = Decimal("-100.00")
    date_of_value = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, date_of_value)
    
    # Act
    positive_price = some_price.positive()
    
    # Assert
    assert positive_price.ccy == currency
    assert positive_price.qty == quantity.__pos__()
    assert positive_price.dov == date_of_value
