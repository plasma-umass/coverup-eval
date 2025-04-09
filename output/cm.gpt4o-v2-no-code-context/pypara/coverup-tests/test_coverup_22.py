# file: pypara/monetary.py:445-448
# asked: {"lines": [445, 446, 447, 448], "branches": []}
# gained: {"lines": [445, 446, 447, 448], "branches": []}

import pytest
from decimal import Decimal, ROUND_HALF_UP
from datetime import date as Date
from pypara.monetary import Money, Currency, SomeMoney

@pytest.fixture
def currency():
    return Currency(
        code='USD',
        name='US Dollar',
        decimals=2,
        type='fiat',
        quantizer=Decimal('0.01'),
        hashcache={}
    )

def test_some_money_round(currency):
    # Setup
    quantity = Decimal('123.456')
    dov = Date(2023, 1, 1)
    some_money = SomeMoney(currency, quantity, dov)
    
    # Test rounding with ndigits less than currency decimals
    rounded_money = some_money.round(1)
    assert rounded_money.qty == Decimal('123.5').quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    assert rounded_money.ccy == currency
    assert rounded_money.dov == dov
    
    # Test rounding with ndigits equal to currency decimals
    rounded_money = some_money.round(2)
    assert rounded_money.qty == Decimal('123.46').quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    assert rounded_money.ccy == currency
    assert rounded_money.dov == dov
    
    # Test rounding with ndigits greater than currency decimals
    rounded_money = some_money.round(3)
    assert rounded_money.qty == Decimal('123.46').quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    assert rounded_money.ccy == currency
    assert rounded_money.dov == dov
