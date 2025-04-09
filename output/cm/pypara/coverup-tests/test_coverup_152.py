# file pypara/monetary.py:689-690
# lines [689, 690]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney

def test_none_money_with_qty():
    none_money = NoneMoney()
    qty = Decimal('10')
    
    # Call with_qty and assert it returns self
    result = none_money.with_qty(qty)
    assert result is none_money, "with_qty should return the NoneMoney instance itself"
