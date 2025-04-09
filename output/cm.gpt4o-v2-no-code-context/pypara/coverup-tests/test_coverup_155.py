# file: pypara/monetary.py:1122-1123
# asked: {"lines": [1123], "branches": []}
# gained: {"lines": [1123], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Price, Currency, SomePrice

def test_someprice_as_integer():
    # Arrange
    currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    quantity = Decimal("123.45")
    date_of_value = Date(2023, 10, 1)
    some_price = SomePrice(ccy=currency, qty=quantity, dov=date_of_value)
    
    # Act
    result = some_price.as_integer()
    
    # Assert
    assert result == 123

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # Add any necessary cleanup code here
