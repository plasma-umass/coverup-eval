# file pypara/monetary.py:1387-1388
# lines [1387, 1388]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import NonePrice

@pytest.fixture
def none_price():
    return NonePrice()

def test_with_qty_returns_self(none_price):
    qty = Decimal('1')
    result = none_price.with_qty(qty)
    assert result is none_price
