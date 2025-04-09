# file: pypara/monetary.py:1129-1131
# asked: {"lines": [1130, 1131], "branches": []}
# gained: {"lines": [1130, 1131], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Price, Currency, SomePrice

def test_someprice_negative():
    # Arrange
    currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    quantity = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_price = SomePrice(currency, quantity, dov)
    
    # Act
    negative_price = some_price.negative()
    
    # Assert
    assert negative_price.ccy == currency
    assert negative_price.qty == -quantity
    assert negative_price.dov == dov
