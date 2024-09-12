# file: pypara/monetary.py:1246-1247
# asked: {"lines": [1246, 1247], "branches": []}
# gained: {"lines": [1246, 1247], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_with_dov():
    # Arrange
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_price = SomePrice(ccy, qty, dov)
    
    # Act
    new_dov = Date(2023, 12, 31)
    new_price = some_price.with_dov(new_dov)
    
    # Assert
    assert new_price.dov == new_dov
    assert new_price.ccy == some_price.ccy
    assert new_price.qty == some_price.qty
