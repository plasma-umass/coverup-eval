# file: pypara/monetary.py:1182-1185
# asked: {"lines": [1182, 1184, 1185], "branches": []}
# gained: {"lines": [1182, 1184, 1185], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from datetime import date as Date

def test_scalar_subtract():
    # Setup
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date.today()
    price = SomePrice(currency, qty, dov)
    
    # Test with int
    result = price.scalar_subtract(10)
    assert result.qty == Decimal("90.00")
    
    # Test with float
    result = price.scalar_subtract(10.5)
    assert result.qty == Decimal("89.50")
    
    # Test with Decimal
    result = price.scalar_subtract(Decimal("10.25"))
    assert result.qty == Decimal("89.75")
    
    # Test with Amount (assuming Amount is a valid type in Numeric)
    # result = price.scalar_subtract(Amount("10.00"))
    # assert result.qty == Decimal("90.00")
    
    # Test with Quantity (assuming Quantity is a valid type in Numeric)
    # result = price.scalar_subtract(Quantity("10.00"))
    # assert result.qty == Decimal("90.00")
