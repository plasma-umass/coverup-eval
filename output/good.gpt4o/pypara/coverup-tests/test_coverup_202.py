# file pypara/monetary.py:1246-1247
# lines [1247]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Price, Currency, SomePrice

def test_someprice_with_dov():
    # Arrange
    currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    quantity = Decimal("100.00")
    original_dov = Date(2023, 1, 1)
    new_dov = Date(2023, 12, 31)
    some_price = SomePrice(currency, quantity, original_dov)
    
    # Act
    updated_price = some_price.with_dov(new_dov)
    
    # Assert
    assert updated_price.ccy == currency
    assert updated_price.qty == quantity
    assert updated_price.dov == new_dov
    assert updated_price != some_price  # Ensure it's a new instance

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Cleanup code if necessary
    yield
    # Add any necessary cleanup steps here
