# file pypara/monetary.py:1013-1020
# lines [1013, 1014, 1018, 1019, 1020]
# branches ['1018->1019', '1018->1020']

import pytest
from decimal import Decimal
from datetime import date as Date
from typing import Optional

# Assuming Currency, NoPrice, and SomePrice are defined somewhere in pypara.monetary
from pypara.monetary import Currency, NoPrice, SomePrice, Price

def test_price_of():
    # Create a mock Currency object
    mock_currency = Currency('USD', 'US Dollar', 2, Decimal('0.01'), None, None)

    # Test case where qty is None
    result = Price.of(ccy=mock_currency, qty=None, dov=Date.today())
    assert result == NoPrice

    # Test case where ccy is None
    result = Price.of(ccy=None, qty=Decimal('10.00'), dov=Date.today())
    assert result == NoPrice

    # Test case where dov is None
    result = Price.of(ccy=mock_currency, qty=Decimal('10.00'), dov=None)
    assert result == NoPrice

    # Test case where all parameters are provided
    qty = Decimal('10.00')
    dov = Date.today()
    result = Price.of(ccy=mock_currency, qty=qty, dov=dov)
    assert isinstance(result, SomePrice)
    assert result.ccy == mock_currency
    assert result.qty == qty
    assert result.dov == dov
