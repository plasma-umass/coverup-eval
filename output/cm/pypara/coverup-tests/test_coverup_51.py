# file pypara/monetary.py:168-175
# lines [168, 169, 175]
# branches []

import pytest
from pypara.monetary import Money
from decimal import Decimal
from numbers import Number

class Numeric(Number):
    def __add__(self, other):
        if isinstance(other, Money):
            return other
        return NotImplemented

class ConcreteMoney(Money):
    def scalar_add(self, other: Numeric) -> "Money":
        if isinstance(other, Numeric):
            return ConcreteMoney()
        return self

@pytest.fixture
def numeric_value():
    return Numeric()

@pytest.fixture
def money_instance():
    return ConcreteMoney()

def test_scalar_add_with_numeric(money_instance, numeric_value):
    result = money_instance.scalar_add(numeric_value)
    assert isinstance(result, Money)

def test_scalar_add_with_non_numeric(money_instance):
    non_numeric = Decimal('10.00')
    result = money_instance.scalar_add(non_numeric)
    assert isinstance(result, Money)
