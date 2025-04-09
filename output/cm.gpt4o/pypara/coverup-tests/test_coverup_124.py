# file pypara/monetary.py:1243-1244
# lines [1243, 1244]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Currency, Price, SomePrice

def test_someprice_with_qty():
    # Arrange
    ccy = Currency("USD", "United States Dollar", 2, Decimal("0.01"), None, None)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_price = SomePrice(ccy, qty, dov)
    
    # Act
    new_qty = Decimal("200.00")
    new_some_price = some_price.with_qty(new_qty)
    
    # Assert
    assert new_some_price.ccy == ccy
    assert new_some_price.qty == new_qty
    assert new_some_price.dov == dov
    assert isinstance(new_some_price, SomePrice)
    assert isinstance(new_some_price, Price)
