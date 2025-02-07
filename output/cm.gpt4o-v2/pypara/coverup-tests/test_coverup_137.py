# file: pypara/monetary.py:919-930
# asked: {"lines": [919, 920, 930], "branches": []}
# gained: {"lines": [919, 920], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Price, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType
from unittest.mock import MagicMock

class TestPrice(Price):
    def __init__(self, ccy=None, qty=None, defined=True):
        self.ccy = ccy
        self.qty = qty
        self.defined = defined

    def is_equal(self, other):
        return self.qty == other.qty and self.ccy == other.ccy

    def as_boolean(self):
        return bool(self.qty)

    def as_float(self):
        return float(self.qty)

    def as_integer(self):
        return int(self.qty)

    def abs(self):
        return TestPrice(self.ccy, abs(self.qty), self.defined)

    def negative(self):
        return TestPrice(self.ccy, -self.qty, self.defined)

    def positive(self):
        return TestPrice(self.ccy, +self.qty, self.defined)

    def round(self, ndigits=0):
        return TestPrice(self.ccy, round(self.qty, ndigits), self.defined)

    def add(self, other):
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        return TestPrice(self.ccy, self.qty + other.qty, self.defined)

    def scalar_add(self, other):
        return TestPrice(self.ccy, self.qty + other, self.defined)

    def subtract(self, other):
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        return TestPrice(self.ccy, self.qty - other.qty, self.defined)

    def scalar_subtract(self, other):
        return TestPrice(self.ccy, self.qty - other, self.defined)

    def multiply(self, other):
        return TestPrice(self.ccy, self.qty * other, self.defined)

    def times(self, other):
        return self.multiply(other)

    def divide(self, other):
        return TestPrice(self.ccy, self.qty / other, self.defined)

    def floor_divide(self, other):
        return TestPrice(self.ccy, self.qty // other, self.defined)

    def lt(self, other):
        if not self.defined:
            return True
        if not other.defined:
            return False
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        return self.qty < other.qty

    def lte(self, other):
        return self.lt(other) or self.is_equal(other)

    def gt(self, other):
        return not self.lte(other)

    def gte(self, other):
        return not self.lt(other)

    def with_ccy(self, ccy):
        return TestPrice(ccy, self.qty, self.defined)

    def with_qty(self, qty):
        return TestPrice(self.ccy, qty, self.defined)

    def with_dov(self, dov):
        return self

    def convert(self, to, asof=None, strict=False):
        return self

    @property
    def money(self):
        return self.qty

    @classmethod
    def of(cls, ccy, qty, dov):
        return cls(ccy, qty)

    def __bool__(self):
        return self.defined

    def __eq__(self, other):
        return self.is_equal(other)

    def __abs__(self):
        return self.abs()

    def __float__(self):
        return self.as_float()

    def __int__(self):
        return self.as_integer()

    def __round__(self, ndigits=0):
        return self.round(ndigits)

    def __neg__(self):
        return self.negative()

    def __pos__(self):
        return self.positive()

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)

    def __floordiv__(self, other):
        return self.floor_divide(other)

    def __lt__(self, other):
        return self.lt(other)

    def __le__(self, other):
        return self.lte(other)

    def __gt__(self, other):
        return self.gt(other)

    def __ge__(self, other):
        return self.gte(other)

def test_lt_undefined_price():
    price1 = TestPrice(defined=False)
    price2 = TestPrice(ccy=Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY), qty=Decimal('10.00'))
    assert price1.lt(price2) is True

def test_lt_incompatible_currency():
    price1 = TestPrice(ccy=Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY), qty=Decimal('10.00'))
    price2 = TestPrice(ccy=Currency.of('EUR', 'Euro', 2, CurrencyType.MONEY), qty=Decimal('10.00'))
    with pytest.raises(IncompatibleCurrencyError):
        price1.lt(price2)

def test_lt_defined_price():
    price1 = TestPrice(ccy=Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY), qty=Decimal('5.00'))
    price2 = TestPrice(ccy=Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY), qty=Decimal('10.00'))
    assert price1.lt(price2) is True
