# file: pypara/monetary.py:689-690
# asked: {"lines": [689, 690], "branches": []}
# gained: {"lines": [689, 690], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney

def test_none_money_with_qty():
    none_money = NoneMoney()
    qty = Decimal('10.00')
    
    result = none_money.with_qty(qty)
    
    assert result is none_money
