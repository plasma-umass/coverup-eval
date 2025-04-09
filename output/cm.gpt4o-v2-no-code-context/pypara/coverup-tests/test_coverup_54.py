# file: pypara/monetary.py:1159-1162
# asked: {"lines": [1159, 1161, 1162], "branches": []}
# gained: {"lines": [1159, 1161, 1162], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, Date

def test_someprice_scalar_add():
    # Setup
    currency = Currency("USD", "United States Dollar", 2, "fiat", Decimal("0.01"), None)
    quantity = Decimal("100.00")
    date_of_value = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, date_of_value)
    
    # Test scalar_add with an integer
    result = some_price.scalar_add(10)
    assert result.ccy == currency
    assert result.qty == quantity + Decimal(10)
    assert result.dov == date_of_value
    
    # Test scalar_add with a float
    result = some_price.scalar_add(10.5)
    assert result.ccy == currency
    assert result.qty == quantity + Decimal(10.5)
    assert result.dov == date_of_value
    
    # Test scalar_add with a Decimal
    result = some_price.scalar_add(Decimal("10.5"))
    assert result.ccy == currency
    assert result.qty == quantity + Decimal("10.5")
    assert result.dov == date_of_value
