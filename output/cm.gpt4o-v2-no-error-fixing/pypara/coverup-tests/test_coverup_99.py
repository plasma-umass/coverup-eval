# file: pypara/monetary.py:1381-1382
# asked: {"lines": [1382], "branches": []}
# gained: {"lines": [1382], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class MockPrice(Price):
    def __init__(self, undefined):
        self.undefined = undefined

    def is_equal(self, other):
        pass

    def as_boolean(self):
        pass

    def as_float(self):
        pass

    def as_integer(self):
        pass

    def abs(self):
        pass

    def negative(self):
        pass

    def positive(self):
        pass

    def round(self, ndigits=0):
        pass

    def add(self, other):
        pass

    def scalar_add(self, other):
        pass

    def subtract(self, other):
        pass

    def scalar_subtract(self, other):
        pass

    def multiply(self, other):
        pass

    def times(self, other):
        pass

    def divide(self, other):
        pass

    def floor_divide(self, other):
        pass

    def lt(self, other):
        pass

    def lte(self, other):
        pass

    def gt(self, other):
        pass

    def gte(self, other):
        pass

    def with_ccy(self, ccy):
        pass

    def with_qty(self, qty):
        pass

    def with_dov(self, dov):
        pass

    def convert(self, to, asof=None, strict=False):
        pass

    @property
    def money(self):
        pass

    @classmethod
    def of(cls, ccy, qty, dov):
        pass

    def __bool__(self):
        pass

    def __eq__(self, other):
        pass

    def __abs__(self):
        pass

    def __float__(self):
        pass

    def __int__(self):
        pass

    def __round__(self, ndigits=0):
        pass

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

@pytest.fixture
def mock_price():
    return MockPrice(undefined=True)

def test_none_price_gte(mock_price):
    none_price = NonePrice()
    assert none_price.gte(mock_price) == True
