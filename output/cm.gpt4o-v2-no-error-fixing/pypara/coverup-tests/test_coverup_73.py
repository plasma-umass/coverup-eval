# file: pypara/monetary.py:1387-1388
# asked: {"lines": [1387, 1388], "branches": []}
# gained: {"lines": [1387, 1388], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NonePrice, Price

def test_none_price_with_qty():
    # Create an instance of NonePrice
    none_price = NonePrice()

    # Call the with_qty method with a Decimal quantity
    result = none_price.with_qty(Decimal('10.0'))

    # Assert that the result is the same instance (self)
    assert result is none_price
