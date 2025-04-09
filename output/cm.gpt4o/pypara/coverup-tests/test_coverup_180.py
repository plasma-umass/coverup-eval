# file pypara/monetary.py:1240-1241
# lines [1241]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomePrice, Currency

def test_someprice_with_ccy():
    # Arrange
    original_ccy = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    new_ccy = Currency(code="EUR", name="Euro", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    qty = Decimal("100.00")
    dov = Date(2023, 10, 1)
    some_price = SomePrice(original_ccy, qty, dov)
    
    # Act
    new_price = some_price.with_ccy(new_ccy)
    
    # Assert
    assert new_price.ccy == new_ccy
    assert new_price.qty == qty
    assert new_price.dov == dov
    assert isinstance(new_price, SomePrice)
