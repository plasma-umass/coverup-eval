# file: pypara/monetary.py:491-494
# asked: {"lines": [491, 493, 494], "branches": []}
# gained: {"lines": [491, 493, 494], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency
from pypara.commons.zeitgeist import Date

class MockCurrency:
    def __init__(self, quantizer):
        self.quantizer = quantizer

    def quantize(self, value):
        return value.quantize(self.quantizer)

@pytest.fixture
def mock_currency():
    return MockCurrency(Decimal('0.01'))

@pytest.fixture
def some_money(mock_currency):
    return SomeMoney(ccy=mock_currency, qty=Decimal('100.00'), dov=Date.today())

def test_scalar_subtract_with_int(some_money):
    result = some_money.scalar_subtract(10)
    assert result.qty == Decimal('90.00')
    assert result.ccy == some_money.ccy
    assert result.dov == some_money.dov

def test_scalar_subtract_with_float(some_money):
    result = some_money.scalar_subtract(10.5)
    assert result.qty == Decimal('89.50')
    assert result.ccy == some_money.ccy
    assert result.dov == some_money.dov

def test_scalar_subtract_with_decimal(some_money):
    result = some_money.scalar_subtract(Decimal('10.55'))
    assert result.qty == Decimal('89.45')
    assert result.ccy == some_money.ccy
    assert result.dov == some_money.dov
