# file pypara/monetary.py:1133-1135
# lines [1133, 1134, 1135]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomePrice, Currency, Price

def test_someprice_positive():
    # Arrange
    currency = Currency(code="USD", name="United States Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    quantity = Decimal("-100.00")
    dov = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, dov)
    
    # Act
    positive_price = some_price.positive()
    
    # Assert
    assert positive_price.ccy == currency
    assert positive_price.qty == quantity.__pos__()
    assert positive_price.dov == dov
