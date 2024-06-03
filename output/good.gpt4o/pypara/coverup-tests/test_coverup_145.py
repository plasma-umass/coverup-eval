# file pypara/monetary.py:1137-1139
# lines [1138, 1139]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Currency, Price, SomePrice

def test_someprice_round():
    # Arrange
    currency = Currency(code="USD", name="United States Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    quantity = Decimal("123.456")
    date_of_value = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, date_of_value)
    
    # Act
    rounded_price = some_price.round(2)
    
    # Assert
    assert rounded_price.ccy == currency
    assert rounded_price.qty == quantity.__round__(2)
    assert rounded_price.dov == date_of_value
