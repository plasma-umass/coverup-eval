# file: pypara/monetary.py:491-494
# asked: {"lines": [491, 493, 494], "branches": []}
# gained: {"lines": [491, 493, 494], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Currency, Date

@pytest.fixture
def some_money():
    ccy = Currency('USD', 'US Dollar', 2, Decimal('0.01'), Decimal('0.01'), None)
    qty = Decimal('100.00')
    dov = Date(2023, 10, 1)
    return SomeMoney(ccy, qty, dov)

def test_scalar_subtract_with_decimal(some_money):
    result = some_money.scalar_subtract(Decimal('10.00'))
    assert result.qty == Decimal('90.00').quantize(some_money.ccy.quantizer)
    assert result.ccy == some_money.ccy
    assert result.dov == some_money.dov

def test_scalar_subtract_with_int(some_money):
    result = some_money.scalar_subtract(10)
    assert result.qty == Decimal('90.00').quantize(some_money.ccy.quantizer)
    assert result.ccy == some_money.ccy
    assert result.dov == some_money.dov

def test_scalar_subtract_with_float(some_money):
    result = some_money.scalar_subtract(10.0)
    assert result.qty == Decimal('90.00').quantize(some_money.ccy.quantizer)
    assert result.ccy == some_money.ccy
    assert result.dov == some_money.dov
