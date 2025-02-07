# file: pypara/monetary.py:674-675
# asked: {"lines": [674, 675], "branches": []}
# gained: {"lines": [674, 675], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class MockMoney(Money):
    def __init__(self, defined):
        self.defined = defined

    def is_equal(self, other):
        return False

    def as_boolean(self):
        return False

    def as_float(self):
        return 0.0

    def as_integer(self):
        return 0

    def abs(self):
        return self

    def negative(self):
        return self

    def positive(self):
        return self

    def round(self, ndigits=0):
        return self

    def add(self, other):
        return self

    def scalar_add(self, other):
        return self

    def subtract(self, other):
        return self

    def scalar_subtract(self, other):
        return self

    def multiply(self, other):
        return self

    def divide(self, other):
        return self

    def floor_divide(self, other):
        return self

    def lt(self, other):
        return False

    def lte(self, other):
        return False

    def gt(self, other):
        return False

    def gte(self, other):
        return False

    def with_ccy(self, ccy):
        return self

    def with_qty(self, qty):
        return self

    def with_dov(self, dov):
        return self

    def convert(self, to, asof=None, strict=False):
        return self

    @property
    def price(self):
        return None

    def __bool__(self):
        return False

    def __eq__(self, other):
        return False

    def __abs__(self):
        return self

    def __float__(self):
        return 0.0

    def __int__(self):
        return 0

    def __round__(self, ndigits=0):
        return self

    def __neg__(self):
        return self

    def __pos__(self):
        return self

    def __add__(self, other):
        return self

    def __sub__(self, other):
        return self

    def __mul__(self, other):
        return self

    def __truediv__(self, other):
        return self

    def __floordiv__(self, other):
        return self

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return False

class TestNoneMoney:
    
    def test_lt(self):
        none_money = NoneMoney()
        other_money = MockMoney(defined=True)
        
        assert none_money.lt(other_money) == True
        
        other_money.defined = False
        
        assert none_money.lt(other_money) == False
