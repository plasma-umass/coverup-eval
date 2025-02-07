# file: pypara/monetary.py:126-131
# asked: {"lines": [126, 127, 131], "branches": []}
# gained: {"lines": [126, 127, 131], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_abs_not_implemented():
    class TestMoney(Money):
        def is_equal(self, other): pass
        def as_boolean(self): pass
        def as_float(self): pass
        def as_integer(self): pass
        def abs(self): return super().abs()
        def negative(self): pass
        def positive(self): pass
        def round(self, ndigits=0): pass
        def add(self, other): pass
        def scalar_add(self, other): pass
        def subtract(self, other): pass
        def scalar_subtract(self, other): pass
        def multiply(self, other): pass
        def divide(self, other): pass
        def floor_divide(self, other): pass
        def lt(self, other): pass
        def lte(self, other): pass
        def gt(self, other): pass
        def gte(self, other): pass
        def with_ccy(self, ccy): pass
        def with_qty(self, qty): pass
        def with_dov(self, dov): pass
        def convert(self, to, asof=None, strict=False): pass
        @property
        def price(self): pass
        def __bool__(self): pass
        def __eq__(self, other): pass
        def __abs__(self): return self.abs()
        def __float__(self): pass
        def __int__(self): pass
        def __round__(self, ndigits=0): pass
        def __neg__(self): pass
        def __pos__(self): pass
        def __add__(self, other): pass
        def __sub__(self, other): pass
        def __mul__(self, other): pass
        def __truediv__(self, other): pass
        def __floordiv__(self, other): pass
        def __lt__(self, other): pass
        def __le__(self, other): pass
        def __gt__(self, other): pass
        def __ge__(self, other): pass

    money_instance = TestMoney()
    with pytest.raises(NotImplementedError):
        money_instance.abs()
