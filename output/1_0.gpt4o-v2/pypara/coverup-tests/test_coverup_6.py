# file: pypara/commons/numbers.py:67-88
# asked: {"lines": [67, 88], "branches": []}
# gained: {"lines": [67, 88], "branches": []}

import pytest
from decimal import Decimal
from pypara.commons.numbers import isum, Amount, Quantity, ZERO, ONE

def test_isum_with_amounts():
    result = isum([Amount(ONE), Amount(ONE)])
    assert result == Amount(Decimal('2'))

def test_isum_with_quantities():
    result = isum([Quantity(ONE), Quantity(ONE)])
    assert result == Quantity(Decimal('2'))

def test_isum_with_amounts_and_start():
    result = isum([Amount(ONE), Amount(ONE)], Amount(ONE))
    assert result == Amount(Decimal('3'))

def test_isum_with_quantities_and_start():
    result = isum([Quantity(ONE), Quantity(ONE)], Quantity(ONE))
    assert result == Quantity(Decimal('3'))

def test_isum_with_default_start():
    result = isum([Decimal('1'), Decimal('2')])
    assert result == Decimal('3')

def test_isum_with_custom_start():
    result = isum([Decimal('1'), Decimal('2')], Decimal('1'))
    assert result == Decimal('4')
