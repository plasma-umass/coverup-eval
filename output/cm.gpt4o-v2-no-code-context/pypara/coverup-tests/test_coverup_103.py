# file: pypara/monetary.py:1240-1241
# asked: {"lines": [1240, 1241], "branches": []}
# gained: {"lines": [1240, 1241], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Currency, Price, SomePrice

@pytest.fixture
def currency_usd():
    return Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)

@pytest.fixture
def currency_eur():
    return Currency(code="EUR", name="Euro", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)

def test_someprice_with_ccy(currency_usd, currency_eur):
    # Arrange
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_price = SomePrice(currency_usd, qty, dov)
    
    # Act
    new_price = some_price.with_ccy(currency_eur)
    
    # Assert
    assert new_price.ccy == currency_eur
    assert new_price.qty == qty
    assert new_price.dov == dov
    assert isinstance(new_price, SomePrice)
