# file: pypara/monetary.py:1243-1244
# asked: {"lines": [1243, 1244], "branches": []}
# gained: {"lines": [1243, 1244], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency
from datetime import date as Date

def test_someprice_with_qty(mocker):
    # Arrange
    currency = mocker.Mock(spec=Currency)
    date = mocker.Mock(spec=Date)
    qty = Decimal("100.00")
    some_price = SomePrice(currency, qty, date)
    
    # Act
    new_qty = Decimal("200.00")
    new_price = some_price.with_qty(new_qty)
    
    # Assert
    assert new_price.qty == new_qty
    assert new_price.ccy == some_price.ccy
    assert new_price.dov == some_price.dov
