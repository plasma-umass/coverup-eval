# file pypara/monetary.py:1116-1117
# lines [1116, 1117]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from collections import namedtuple

# Mocking Currency and Date as they seem to require additional arguments
Currency = namedtuple('Currency', ['code'])
Date = namedtuple('Date', ['year', 'month', 'day'])

def test_someprice_as_boolean():
    # Mocking Currency and Date for the purpose of the test
    currency = Currency(code='USD')
    date = Date(year=2023, month=1, day=1)
    
    # Test with qty as 0, expecting as_boolean to return False
    price_zero = SomePrice(ccy=currency, qty=Decimal('0'), dov=date)
    assert not price_zero.as_boolean()
    
    # Test with qty as non-zero, expecting as_boolean to return True
    price_non_zero = SomePrice(ccy=currency, qty=Decimal('10'), dov=date)
    assert price_non_zero.as_boolean()
