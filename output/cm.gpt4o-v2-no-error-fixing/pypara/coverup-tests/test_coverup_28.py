# file: pypara/monetary.py:369-371
# asked: {"lines": [369, 370, 371], "branches": []}
# gained: {"lines": [369, 370], "branches": []}

import pytest
from abc import ABC, abstractmethod
from pypara.monetary import Money

class ConcreteMoney(Money):
    def is_equal(self, other):
        return isinstance(other, ConcreteMoney)
    
    def as_boolean(self):
        return True
    
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
        return self
    
    def __bool__(self):
        return True
    
    def __eq__(self, other):
        return isinstance(other, ConcreteMoney)
    
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

def test_pos_method():
    money_instance = ConcreteMoney()
    result = +money_instance
    assert result is money_instance
