# file: pypara/monetary.py:1030-1032
# asked: {"lines": [1030, 1031, 1032], "branches": []}
# gained: {"lines": [1030, 1031], "branches": []}

import pytest
from decimal import Decimal
from unittest.mock import MagicMock
from pypara.monetary import Price
from pypara.currencies import Currency
from pypara.commons.zeitgeist import Date

class ConcretePrice(Price):
    def __abs__(self):
        return self

    def is_equal(self, other):
        return isinstance(other, Price)

    def as_boolean(self):
        return True

    def as_float(self):
        return 1.0

    def as_integer(self):
        return 1

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

    def times(self, other):
        return self

    def divide(self, other):
        return self

    def floor_divide(self, other):
        return self

    def lt(self, other):
        return True

    def lte(self, other):
        return True

    def gt(self, other):
        return True

    def gte(self, other):
        return True

    def with_ccy(self, ccy):
        return self

    def with_qty(self, qty):
        return self

    def with_dov(self, dov):
        return self

    def convert(self, to, asof=None, strict=False):
        return self

    @property
    def money(self):
        return self

    def __bool__(self):
        return True

    def __eq__(self, other):
        return isinstance(other, Price)

    def __float__(self):
        return 1.0

    def __int__(self):
        return 1

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
        return True

    def __le__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True

@pytest.fixture
def price():
    return ConcretePrice()

def test_abs(price):
    result = abs(price)
    assert result is price
