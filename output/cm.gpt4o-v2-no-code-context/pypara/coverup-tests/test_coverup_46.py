# file: pypara/monetary.py:548-550
# asked: {"lines": [548, 549, 550], "branches": []}
# gained: {"lines": [548, 549, 550], "branches": []}

import pytest
from decimal import Decimal, ROUND_HALF_EVEN
from datetime import date as Date
from pypara.monetary import Money, Currency, SomeMoney

@pytest.fixture
def some_money():
    ccy = Currency('USD', 'US Dollar', 2, Decimal, Decimal('0.01'), None)
    qty = Decimal('100.00')
    dov = Date(2023, 1, 1)
    return SomeMoney(ccy, qty, dov)

def test_with_qty(some_money):
    new_qty = Decimal('200.00')
    new_money = some_money.with_qty(new_qty)
    
    assert new_money.qty == new_qty.quantize(some_money.ccy.quantizer, rounding=ROUND_HALF_EVEN)
    assert new_money.ccy == some_money.ccy
    assert new_money.dov == some_money.dov
